import unittest

from solutions.kyu4_strip_comments import solution

class SampleTests(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
        self.assertEqual(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")

if __name__ == '__main__':
    unittest.main()