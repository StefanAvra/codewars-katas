import unittest

from solutions.kyu5_valid_parentheses import valid_parentheses

class SampleTests(unittest.TestCase):

    def test_valid_parentheses(self):
        self.assertEqual(valid_parentheses("  ("),False)
        self.assertEqual(valid_parentheses(")test"),False)
        self.assertEqual(valid_parentheses(""),True)
        self.assertEqual(valid_parentheses("hi())("),False)
        self.assertEqual(valid_parentheses("hi(hi)()"),True)

if __name__ == '__main__':
    unittest.main()