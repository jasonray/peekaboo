import time
import signal
import os


def main():
    ghost = Ghost(60)
    ghost.start()

class Ghost:
    alive_time = None
    shutdown_requested = False

    def __init__(self, alive_time_seconds):
        self.alive_time=alive_time_seconds
        signal.signal(signal.SIGABRT, self.handler)

    def start(self):
        print("starting ghost")
        print("- alive_time", self.alive_time)
        print("pid", os.getpid() )

        continue_process=True
        start_time = time.time()
        print("start time", start_time)
        while continue_process:
            now_time = time.time()
            delta = round(now_time - start_time,2)
            print(f"[delta:{delta}]")
            if delta>self.alive_time:
                continue_process=False
            else:
                time.sleep(1)
            if self.shutdown_requested:
                print('shutdown request recognized')
                continue_process=False
        print("complete")

    def handler(self, signum, frame):
        print(f'received signal [{signum}]')
        if signum == 6:
            self.shutdown_requested = True
            print('shutdown requested', self.shutdown_requested)

if __name__ == "__main__":
    main()