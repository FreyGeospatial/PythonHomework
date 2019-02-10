"""
Jordan Frey
Python Programming
Homework 23, Question 1
"""


# Input number of rows and columns and display array

def q1(iValRow, iValCol):
   i = 1
   # Complete after nested while loop runs through all iterations
   while i <= iValRow:
      j = 1

      # Complete with each iteration of parent while loop
      while j <= iValCol:
         print j ** i, '\t', #remember this comma!
         j = j + 1
      print '\n'
      i = i + 1

#Execute example
q1(3, 5)
