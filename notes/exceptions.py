def inputNumber():
    x = input('Pick a number: \n')
    if x == 17:
        raise ValueError, '17 is a bad number'
    return x

print inputNumber()
