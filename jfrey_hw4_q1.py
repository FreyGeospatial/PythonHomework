# Jordan Frey
# Python Programming
# Homework 4, question 1

# Write a program to calculate the scores that an athlete receives in a
# competition from five judges. The following rule is applied in the calculation:
# two scores, one lowest and one highest, must be excluded from the total scores
# (in other words, there are only three valid scores to add up).

myString = "8.9, 9.9, 9.5, 9.7, 7.8"
myString = myString.split(", ")
for i in range(len(myString)):
    myString[i] = float(myString[i])

answer = sum(myString) - min(myString) - max(myString)
print answer