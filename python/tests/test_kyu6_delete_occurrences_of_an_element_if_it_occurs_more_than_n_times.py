import unittest

from solutions.kyu6_delete_occurrences_of_an_element_if_it_occurs_more_than_n_times import delete_nth

class SampleTests(unittest.TestCase):

    def test_delete_nth(self):
        self.assertEqual(delete_nth([20,37,20,21], 1), [20,37,21])
        self.assertEqual(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])

if __name__ == '__main__':
    unittest.main()