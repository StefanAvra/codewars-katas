"""
Beginner Series #1 School Paperwork

Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need.

Example:
paperwork(5, 5) == 25
Note: if n < 0 or m < 0 return 0!

Waiting for translations and Feedback! Thanks!


"""

def paperwork(n, m):
    if n > 0 and m > 0:
        total = n * m
    else:
        total = 0
    return total
