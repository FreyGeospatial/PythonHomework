import os
wd = r"D:\OneDrive\Documents\School Work\Clark\Python" # string literal (raw)
directory_list = os.listdir(wd)

for i in range(len(directory_list)):
    print directory_list[i]

strName = r'\myTestFile.txt'

# open file
strPathName = wd + strName
f = open(strPathName, 'r')
f.read() #read entire file
f.read(5) # acts as cursor, needs to reset search
f.seek(0)
f.readlines() #inserts text into a list
f.seek(0)
f.readline() #reads the current line the cursor is on

#iterate through text file lines:
f.seek(0)
for i in f.readlines():
    print i

f = open(strPathName, 'a')
f.write('\nMassachusetts is in the USA.')
f.close()

f = open(strPathName, 'r') #must be set back to 'r'; 'a' will not read
f.seek(0)
for i in f.readlines():
    print i
