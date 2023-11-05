import unittest
from src.ghost import Ghost


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
