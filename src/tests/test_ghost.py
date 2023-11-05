import unittest
from src.ghost import Ghost
import time


class TestGhost(unittest.TestCase):

    def test_construct(self):
        ghost = Ghost(ttl=5, sleep_duration=10)
        self.assertIsNotNone(ghost)

    def test_ttl(self):
        ghost = Ghost(ttl=5, sleep_duration=10)
        self.assertEqual(ghost.ttl, 5)

    def test_ttl_default(self):
        ghost = Ghost(sleep_duration=10)
        self.assertEqual(ghost.ttl, 0)

    def test_sleep_duration(self):
        ghost = Ghost(ttl=5, sleep_duration=10)
        self.assertEqual(ghost.sleep_duration, 10)

    def test_sleep_duration_default(self):
        ghost = Ghost(ttl=5)
        self.assertEqual(ghost.sleep_duration, 0)

    def test_start(self):
        ttl = 2
        sleep_duration = 1
        precision = 1
        ghost = Ghost(ttl=ttl, sleep_duration=sleep_duration)
        start_time = time.time()
        ghost.start()
        end_time = time.time()
        delta = end_time - start_time
        print(f'[start={round(start_time,1)}][end={round(end_time,1)}][delta={round(delta,1)}]')
        self.assertTrue(delta >= ttl)
        self.assertTrue(delta <= ttl + precision)
