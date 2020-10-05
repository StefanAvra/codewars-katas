import unittest

from solutions.kyu6_arrh_grabscrab import grabscrab

class SampleTests(unittest.TestCase):

    def test_grabscrab(self):
        self.assertEqual(grabscrab("trisf", ["first"]), ["first"], "Should have found 'first'")
        self.assertEqual(grabscrab("oob", ["bob", "baobab"]), [], "Should not have found anything")
        self.assertEqual(grabscrab("ainstuomn", ["mountains", "hills", "mesa"]), ["mountains"], "Should have found 'mountains'")
        self.assertEqual(grabscrab("oolp", ["donkey", "pool", "horse", "loop"]), ["pool", "loop"], "Should have found 'pool' and 'loop'")
        self.assertEqual(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]), ["sport", "ports"], "Should have found 'sport' and 'ports'")
        self.assertEqual(grabscrab("ourf", ["one","two","three"]), [], "Should not have found anything")

if __name__ == '__main__':
    unittest.main()