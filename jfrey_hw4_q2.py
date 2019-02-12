# Jordan Frey
# Python Programming
# Homework 4, Question 2

# In a health awareness campaign at a university, competing teams are formed to keep track of team members
# steps walked daily, within a three-day period. At the end of this campaign,
# the winning team is a team that has the highest average daily walking steps.

# Write a program to identify the winner by outputting the teams name and its average daily walking steps.


d1 = {'Random Walkers': 8795, 'Clark4TheRoad': 8939,
'Team Goddard': 8953, 'TerrSet Team': 11033,
'Corner Walkers': 21879, 'Team Dynamo': 13089,
'Life is a Highway': 22020}

d2 ={'Random Walkers': 13199, 'Clark4TheRoad': 18939,
'Team Goddard': 15080, 'TerrSet Team': 12345,
'Corner Walkers': 9800, 'Team Dynamo': 23290,
'Life is a Highway': 12007}

d3 = {'Random Walkers': 10002, 'Clark4TheRoad': 13447,
'Team Goddard': 13353,
'TerrSet Team': 22345, 'Corner Walkers': 21879,
'Team Dynamo': 9119, 'Life is a Highway': 7897}

myList = d1.keys()

myDict =  {'Random Walkers': 0, 'Clark4TheRoad':0,
          'Team Goddard':0, 'TerrSet Team':0,
          'Corner Walkers':0, 'Team Dynamo':0,
          'Life is a Highway':0}



for i in range(len(myList)):
   myDict[myList[i]] = (d1[myList[i]] + d2[myList[i]] + d3[myList[i]]) / 3

print "The winning team is: " + max(myDict)