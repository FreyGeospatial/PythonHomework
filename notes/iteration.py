# multiplication table
def multi_table(max_i, max_j):
    i = 1
    while i <= max_i:
        j = 1
        while j <= max_j:
            print i * j, "\t"
            j += 1
        print "\n"
        i += 1

i = 1
x = 0
while i <= 20:
    if i % 5 == 0:
        x += i
    i += 1
print x
