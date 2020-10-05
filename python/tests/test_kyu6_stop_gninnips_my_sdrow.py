import unittest

from solutions.kyu6_stop_gninnips_my_sdrow import spin_words

class SampleTests(unittest.TestCase):

    def test_spin_words(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")


if __name__ == '__main__':
    unittest.main()