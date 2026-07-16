import unittest
from tvcontroller import TVController, CHANNELS


class TestTVController(unittest.TestCase):

    def setUp(self):
        self.tv = TVController(CHANNELS)

    def test_first_channel(self):
        self.assertEqual(self.tv.first_channel(), 'BBC')

    def test_last_channel(self):
        self.assertEqual(self.tv.last_channel(), 'TV1000')

    def test_current_channel(self):
        self.tv.turn_channel(2)
        self.assertEqual(self.tv.current_channel(), 'Discovery')

    def test_turn_channel(self):
        self.assertEqual(self.tv.turn_channel(3), 'TV1000')

    def test_turn_channel_first(self):
        self.assertEqual(self.tv.turn_channel(1), 'BBC')

    def test_next_channel(self):
        self.tv.first_channel()
        self.assertEqual(self.tv.next_channel(), 'Discovery')
        self.assertEqual(self.tv.next_channel(), 'TV1000')

    def test_next_channel_loop(self):
        self.tv.last_channel()
        self.assertEqual(self.tv.next_channel(), 'BBC')
        self.assertEqual(self.tv.next_channel(), 'Discovery')

    def test_previous_channel(self):
        self.tv.first_channel()
        self.assertEqual(self.tv.previous_channel(), 'TV1000')

    def test_exist_str(self):
        self.assertEqual(self.tv.exists('TV1000'), 'Yes')
        self.assertEqual(self.tv.exists('BBC'), 'Yes')
        self.assertEqual(self.tv.exists('MTV'), 'No')

    def test_exist_int(self):
        self.assertEqual(self.tv.exists(0), 'No')
        self.assertEqual(self.tv.exists(1), 'Yes')
        self.assertEqual(self.tv.exists(3), 'Yes')
        self.assertEqual(self.tv.exists(10), 'No')


if __name__ == '__main__':
    unittest.main()
