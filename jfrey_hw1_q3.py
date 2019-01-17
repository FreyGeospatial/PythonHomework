# Jordan Frey
# Python Programming
# Homework 1: Question 1

# Calculate area and volume based using only two parameters for each function


# define calc_area function
def calc_area(l, w):
    result = l * w
    return result  # does not print result unless you specify: print calc_area


# define calc_volume function using only two parameters: area and thickness
def calc_volume(a, t):
    result = a * t
    return result


# call and print calc_area and calc_volume function
print "The area of my rectangle is: ", calc_area(5, 3.0)
print "The volume of my cuboid is: ", calc_volume(calc_area(5, 3.0), 2)
