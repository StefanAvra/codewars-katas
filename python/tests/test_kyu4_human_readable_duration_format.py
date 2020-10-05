import unittest

from solutions.kyu4_human_readable_duration_format import format_duration

class SampleTests(unittest.TestCase):

    def test_format_duration(self):
        self.assertEqual(format_duration(1), "1 second")
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
        self.assertEqual(format_duration(120), "2 minutes")
        self.assertEqual(format_duration(3600), "1 hour")
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")

if __name__ == '__main__':
    unittest.main()