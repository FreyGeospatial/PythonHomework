# Import modules


import math as m


'''
Create function to find pythagorean theorem.
'''


def distance(x1, y1, x2, y2):
    answer = m.sqrt((x2 - x1) ** 2) + ((y2-y1) ** 2)
    return answer


# Example of recurssion (when a function calls itself)
def countdown(n):
    if n == 0:
        print "BLASTOFF"
    else:
        print n
        countdown(n-1)


# Recursive Python function that returns the sum of the first n positive integers

def sum_int(n):
    if n == 1:
        return 1
    elif n < 0 or isinstance(n, float):
        return "Not a positive integer"
    else:
        return n + sum_int(n-1)


x = 10
while x > 0:
    print x
    x = x - 1