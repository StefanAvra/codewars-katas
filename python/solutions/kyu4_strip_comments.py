"""
Strip Comments

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

"""

def solution(string, markers):
    lines = string.splitlines()
    result = []
    for line in lines:
        tlines = []
        if markers:
            for marker in markers:
                if marker in line:
                    tlines.append(line[0:line.index(marker)])
                else:
                    tlines.append(line)
            result.append(sorted(tlines, key=len)[0].strip())
        else:
            result = lines
    return '\n'.join(result)
