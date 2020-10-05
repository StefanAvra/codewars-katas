import unittest

from solutions.kyu6_what_color_is_your_name import string_color

class SampleTests(unittest.TestCase):

    def test_string_color(self):
        self.assertEqual(string_color("Jack"), "79CAE5")
        self.assertEqual(string_color("John Doe"), "C70033")
        self.assertEqual(string_color("CodeWars"), "182892")
        self.assertEqual(string_color("X"), None)

if __name__ == '__main__':
    unittest.main()