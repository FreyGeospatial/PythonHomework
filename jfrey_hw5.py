# Jordan Frey
# Python Programming
# Homework 5
# 2/23/19

# Set path to read and save files to
path = "D:\\OneDrive\\Documents\\School Work\\Clark\\Python\\Lab 5 Assignment and Data"
# name of 2017 file
filename2 = r'\\Lab5_2017data.csv'
# open 2017 file for reading
f2 = open(path + filename2, 'r')
# read file into new variable
contents2 = f2.read() # read file into a string
# split contents from single string to list of strings using comma as delimiter
contents2_list = contents2.split(",")


# same as above but for 2018 data
filename1 = r'\\Lab5_2018_data.csv'
f1 = open(path + filename1, 'r')
contents1 = f1.read() # read file into a string
contents1_list = contents1.split(",") # split string into list using comma as delimiter

# set name for output text file
output_path_name = path + r"\myOutput.txt"

# create new file
f3 = open(output_path_name, 'w')

# start writing the file
f3.write("School ID" + "\t" +
         "# of students (18)" + "\t" +
         "# of students (17)" + "\t" +
         "growth" + "\n")

# write items from csv files into proper format
for i in range(0, len(contents1_list)):
    if i % 2 == 0:
        f3.write(contents1_list[i] + "\t\t" +
                 contents1_list[i+1] + "\t\t\t" +
                 contents2_list[i+1] + "\t\t\t" +
                 str(int(contents2_list[i+1]) - int(contents1_list[i+1])))
        f3.write("\n")

# separate data values from data summary
f3.write("-" * 70)
f3.write("\n")

# create empty lists to contain summarized values
summation17 = []
summation18 = []

# append summarized values to empty lists
for i in range(0, len(contents1_list)):
    if i % 2 != 0:
        summation18.append(int(contents1_list[i]))
        summation17.append(int(contents2_list[i]))

# write summarized values to text file
f3.write("Total:" + "\t\t" + str(sum(summation18)) +
         "\t\t\t" + str(sum(summation17)) + "\t\t\t" +
         str(int(sum(summation18) - sum(summation17))))

# add total growth to new variable to ease programming
totalGrowth = int(sum(summation18) - sum(summation17))


f3.write("\n\n")
f3.write("Total Growth Rate: ")

# write growth rate to file
f3.write(str(format(totalGrowth / float(sum(summation17)) * 100, '.2f')) + "%")


# close and save file
f3.close()

# close external data files
f1.close()
f2.close()

