"""
Jordan Frey
Python Programming
Homework 2, Question 1
"""


"""
Write a program with a function called feel_temp(). The function
converts a given temperature in Celsius into four categorical levels- hot,
warm, cool, and ocld using a set criteria. The program must promp the
user to input a temperature.
"""

# Create feel_temp() function


def feel_temp():
    # input an integer for degrees celsius, coerce to integer,
    # and if invalid number return error.
    try:
        x = int(raw_input("Enter a temperature in degrees celsius: "))
        # Conditional statements
        if x > 35:
            return "Hot"
        elif x >= 20:
            return "Warm"
        elif x >= 10:
            return "Cool"
        else:
            return "Cold"
    except ValueError:
        print "Please enter a valid number."


feel_temp()
