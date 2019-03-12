# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:17:41 2019

@author: JFrey
"""

#generates list of random numbers
import random
def rand_list(n):
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
    return s

contents=(rand_list(int(input('Enter number of input items here:  '))))

#set number of bins
b = int(input('Enter number of bins here:  '))


#Sorts values & creates bins
binwidth = 1.0/b
newdict={}

for x in range (0,b):
    y=0
    for item in contents:
        if item >=x*binwidth and item < ((x+1)*binwidth):
            y+=1
    newdict[x]=y

#Prints the number of items in each bin
print (' ')
for item in range(0,b):
    print ('Total random numbers in bin', item+1, 'are', newdict[item])