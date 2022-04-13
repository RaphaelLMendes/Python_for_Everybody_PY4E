'''
Exercise 2: Write a program to look for lines of the form:

    New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method. 
Compute the average of the numbers and print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
'''

import re

file = str(input("Enter file: "))

# opening the file and creating a handler object
#fhand = open('../../files/mbox.txt', 'r')

fhand = open(f'../../files/{file}', 'r')

values = []

# loop through each line in the file
for line in fhand:
    # removing whitespaces ( \n at the end of each line)
    line = line.rstrip()
    array_occ = re.findall('^New Revision: ([0-9]*)', line)
    for item in array_occ:
        values.append(int(item))

print(int(sum(values)/len(values)))