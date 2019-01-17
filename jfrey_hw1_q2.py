# Jordan Frey
# Python Programming
# Homework 1: Question 1

# Calculate volume based on parameters: thickness, width, height


# define calc_volume function
def calc_volume(t, w, h):
    result = t * w * h
    print "Plywood description:"
    print "Height is: ", h
    print "Width is: ", w
    print "Thickness is :", t
    print "Volume is: ", result


# call calc_volume function with three arguments
calc_volume(7.75, 2.25, 5.0/12.0)
