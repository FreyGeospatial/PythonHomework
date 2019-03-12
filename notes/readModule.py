# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:53:23 2019

@author: JFrey
"""

#Pure functions vs modifiers

#pure functions do not modify the object, and just return an output
#modifiers modify the object being passed onto it

import os
os.chdir("D:\OneDrive\Documents\School Work\BCC\INF103")

import dollar_display
import NJ_lottery_pick2
import wc

wc.linecount('NJ_lottery_pick2.py')

#########################
#########################
#recursion example

def countdown(n):
    if n <= 0:
        print("sup")
    else:
        print(n)
        countdown(n-1)
        
        