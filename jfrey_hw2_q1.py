"""
Jordan Frey
Python Programming
Homework 2, Question 1
"""

'''
Tests whether one integer is divisible by another. The user will be prompted to enter two numbers
(a numerator and a denominator). If the first number is evenly divisible by the second
number, the program returns the Boolean value True. If not, the program returns the value False.
'''


# Create function divisible_truefalse:


def divisible_truefalse():
    # ask user input for numerator and denominator variables
    numerator = float(raw_input("Input numerator: "))
    denominator = float(raw_input("Input denominator: "))

    # if input is evenly divisible, return true
    if (float(numerator) / float(denominator)) == int(float(numerator) / float(denominator)):
        return True
    else:
        return False


divisible_truefalse()

