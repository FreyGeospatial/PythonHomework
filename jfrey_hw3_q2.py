"""
Jordan Frey
Python Programming
Homework 3, Question 2
"""

"""
Write a function called count_digit(str_input) to count the 
occurrence of digits in the input string. You need to utilize 
the for loop in this function. 
"""

def count_digit(str_input):
    x = 0
    for i in range(len(str_input)): #for every iteration in the length of the input
        for j in range(10): #compare the value of i to the current iteration of j
            if str_input[i] == str(j):
                x = x + 1
    return x

count_digit("950 Main Street")
count_digit("1600 pennsylvania ave. nw Washington, DC 20500")

