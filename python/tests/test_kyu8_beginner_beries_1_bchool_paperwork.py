import unittest

from solutions.kyu8_beginner_beries_1_bchool_paperwork import paperwork

class SampleTests(unittest.TestCase):

    def test_paperwork(self):
        self.assertEqual(paperwork(5,5), 25, "Failed at Paperwork(5,5)")


if __name__ == '__main__':
    unittest.main()
