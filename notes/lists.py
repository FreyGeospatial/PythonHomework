# A list can be heterogeneous

myList = ["word", 12, 55.2, [10, 3]]
print(myList[1])
print(myList[0])
print(myList[3])
print(myList[3][1])


myRange = range(10)
print(myRange)
myRange2 = list(range(10))
print(myRange2)

total = 0
for number in range(100):
    if number % 2 == 0:
        total += number
print(total)

for number in range(100):
    print(number)

testList = []
for i in range(20):
    testList.append(i)
print(testList)

places = ['Boston', 'Worcester', 'natick']
print(places[0])
print(places[-1:])
places[2] = 'WPI'
print(places)
print(places[-2:])
places[-2:] = "Howdy"
print(places)



list1 = ['a', 'd', 'c']
print(list1[1:2])
print(list1[1:3])

list1[1] = ['b', 'c']
print(list1)

list1[1:1] = ['b']
print(list1) # inserts item into list
del list1[2] # does not require reassignment

list1.append('d')
print(list1)


t2 = ['e', 'f']

list1.append(t2)
print(list1)

del list1[4]

list1.extend(t2)
print(list1)


list1copy = list1
id(list1)
id(list1copy)
del list1[0]
print(list1copy)

list1[0:0] = 'a'

list1_deep_copy = list1[:]
id(list1_deep_copy) == id(list1copy)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]