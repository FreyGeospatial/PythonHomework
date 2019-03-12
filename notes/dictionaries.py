# key-value

inventory = {'apples':430, 'bananas':312}
inventory['oranges'] = 525
inventory['pears'] = 217
inventory
del inventory['pears']
len(inventory)

inventory.keys()
inventory.values()
inventory.items()
inventory['bananas']

sizes = {'S':28, 'M':32, 'L':36, 'XL':40}
size_new = sizes.copy

matrix2 = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

matrix3 = {(0,3): 1, (2, 1): 2, (4, 3): 3}
matrix3.get((0,3), 0) #1st is the key, 2nd is the value to return if False 
matrix3.get((1,3), 0)
matrix3.get((1,3), 'F')
