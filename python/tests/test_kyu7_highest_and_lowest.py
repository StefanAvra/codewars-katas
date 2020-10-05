import unittest

from solutions.kyu7_highest_and_lowest import high_and_low

class SampleTests(unittest.TestCase):

    def test_high_and_low(self):
        self.assertEqual(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")


if __name__ == '__main__':
    unittest.main()