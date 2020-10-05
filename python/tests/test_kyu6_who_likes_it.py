import unittest

from solutions.kyu6_who_likes_it import likes

class SampleTests(unittest.TestCase):

    def test_likes(self):
        self.assertEqual(likes([]), 'no one likes this')
        self.assertEqual(likes(['Peter']), 'Peter likes this')
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')


if __name__ == '__main__':
    unittest.main()