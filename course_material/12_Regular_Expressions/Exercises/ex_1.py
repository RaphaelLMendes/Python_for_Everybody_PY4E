'''
Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$
'''

import re

user_re = str(input("Enter a regular expression: "))

# opening the file and creating a handler object
fhand = open('../../files/mbox.txt', 'r')

count_lines = 0

# loop through each line in the file
for line in fhand:
    # removing whitespaces ( \n at the end of each line)
    line = line.rstrip()
    array_occ = re.findall(f'{user_re}', line)
    if len(array_occ) > 0:
        count_lines += 1

print(f'mbox.txt had {count_lines} lines that matched {user_re}')