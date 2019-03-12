print bool(4 == 5) # false
print 4 > 3  # true
print bool(4)  # true
print bool(1)  # true
print bool(2)  # true
print bool(0)  # false
print bool(-1)  # true
print bool("")  # false
print bool(" ")  # true
print bool("False")  # True
print bool(False)  # false
print bool("True")  # true
print bool(True)  # true
print bool(None)  # false
print bool()  # False

if "1":
    print "Truthy"


isinstance(2, int)
isinstance(2, str)
isinstance('2', int)
isinstance('2', str)
isinstance(2, float)
isinstance(2.0, float)

x = 0
if x > 0:
    print x, "is positive"
elif x == 0:
    print x, "is not negative or positive"
else:
    print x, "is negative"


def even_odd(x):
    if (x % 2) == 0:
        print x, "is even"
    elif (x % 2) == 1:
        print x, "is odd"
    else:
        print "pass an integer!"


name = raw_input("What is your name? ")
age = int(raw_input("How old are you? "))