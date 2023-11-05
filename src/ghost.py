import time
import signal
import os
import argparse
import datetime


def main():
    # Initialize parser
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--ttl", dest="ttl", default=0, help="Specifies the amount of time (in seconds) to keep ghost alive")
    parser.add_argument("-s", "--sleep", dest="sleep_duration", default=1, help="How often to check for closing process")
    args = parser.parse_args()

    ghost = Ghost(args.ttl, args.sleep_duration)
    ghost.start()


class Ghost:
    _ttl = None
    _sleep_duration = None
    _shutdown_requested = False
    _start_time = None

    def __init__(self, ttl, sleep_duration):
        self.ttl = ttl
        self.sleep_duration = sleep_duration
        signal.signal(signal.SIGABRT, self.signal_handler)

    @property
    def ttl(self):
        return self._ttl

    @ttl.setter
    def ttl(self, value):
        self._ttl = int(value)

    @property
    def sleep_duration(self):
        return self._sleep_duration

    @sleep_duration.setter
    def sleep_duration(self, value):
        self._sleep_duration = int(value)

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def shutdown_requested(self):
        return self._shutdown_requested

    @shutdown_requested.setter
    def shutdown_requested(self, value):
        self._shutdown_requested = bool(value)

    @property
    def uptime(self):
        now_time = time.time()
        delta = now_time - self.start_time
        return delta

    def is_expired(self):
        if self.ttl == 0:
            return False
        else:
            return self.uptime > self.ttl

    @property
    def pid(self):
        return os.getpid()

    def start(self):
        self.log("starting ghost")
        self.log("- ttl", self.ttl)
        self.log("- sleep_duration", self.sleep_duration)
        self.log("pid", self.pid)

        continue_process = True
        self.start_time = time.time()
        self.log("start time", self.start_time)
        while continue_process:
            self.log(f"[uptime:{round(self.uptime,1)}]")
            if self.shutdown_requested:
                self.log('shutdown request recognized')
                continue_process = False
            elif self.is_expired():
                self.log('expired')
                continue_process = False
            else:
                time.sleep(self.sleep_duration)
        self.log(f"process complete [uptime={round(self.uptime,1)}]")

    def signal_handler(self, signum, frame):
        self.log(f'received signal [{signum}]')
        if signum == 6:
            self.shutdown_requested = True
            self.log('shutdown requested')

    def log(self, *messages):
        message_buffer = []
        for message_entry in messages:
            message_buffer.append(str(message_entry))
        message = ' '.join(message_buffer)
        timestamp = datetime.datetime.now()
        print(f'{timestamp}\t{self.pid}\t{message}')


if __name__ == "__main__":
    main()
