import re
import os

def create_solution_file(kata_name):
    kata_file = get_valid_filename(kata_name)

    if not os.path.exists(f'../solutions/{kata_file}.py'):
        with open(f'../solutions/{kata_file}.py', 'w') as f:
            content = '\"\"\"\ntitle\ndescription\n\"\"\"\n\ndef func():\n    pass'
            f.write(content)

def create_test_file(kata_name):
    kata_file = get_valid_filename(kata_name)

    if not os.path.exists(f'../tests/test_{kata_file}.py'):
        with open(f'../tests/test_{kata_file}.py', 'w') as f: 
            content = f'import unittest\n\nfrom solutions.{kata_file} import func\n\nclass SampleTests(unittest.TestCase):\n\n    def test_func(self):\n    pass\n\nif __name__ == \'__main__\':\n    unittest.main()'
            f.write(content)

def create_kata_files(kata_name):
    create_solution_file(kata_name)
    create_test_file(kata_name)

def get_valid_filename(s):
    """
    Return the given string converted to a string that can be used for a clean
    filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot.
    >>> get_valid_filename("john's portrait in 2004.jpg")
    'johns_portrait_in_2004.jpg'
    """
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s).lower()


