path = "D:\\OneDrive\\Documents\\School Work\\Clark\\Python\\notes"
filename = r'\\Data.csv'
f = open(path+filename, 'r')
contents = f.read()
f.close()

contents.split(",")

