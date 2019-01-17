# Jordan Frey
# Python Programming
# Homework 1: Question 1

# Calculate the area and perimeter of a [two-equal sided] trapezoid and output result to console


# import modules
import math as m


# define single function to calculate area and perimeter of trapezoid
def calc_area_perimeter(b1, b2, h):
    area = ((b1 + b2) / 2.0) * h
    # use of absolute value allows b1 and b2 arguments to be input w/out attention to order
    perimeter = (m.sqrt((abs(b1-b2)/2.0)**2 + h**2)*2) + b1 + b2
    print "The area of the trapezoid is: ", area
    print "The perimeter of the trapezoid is: ", perimeter


# call function
calc_area_perimeter(3, 5, 2)
