import unittest

from solutions.kyu6_does_my_number_look_big_in_this import narcissistic

class SampleTests(unittest.TestCase):

    def test_narcissistic(self):
        self.assertEqual(narcissistic(7), True, '7 is narcissistic');
        self.assertEqual(narcissistic(371), True, '371 is narcissistic');
        self.assertEqual(narcissistic(122), False, '122 is not narcissistic')
        self.assertEqual(narcissistic(4887), False, '4887 is not narcissistic')

if __name__ == '__main__':
    unittest.main()