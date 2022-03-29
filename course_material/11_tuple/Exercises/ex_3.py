'''
Exercise 3: 

Write a program that reads a file and prints the letters in decreasing order of frequency. 
Your program should convert all the input to lower case and only count the letters a-z. 
Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
Find text samples from several different languages and see how letter frequency varies 
between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

'''

import re

# opening the file and creating a handler object
fhand = open('../../files/romeo.txt', 'r')

# creating the disctionairy to be able to count occurrences
count = {}

# loop through each line in the file
for line in fhand:

    # removing whitespaces ( \n at the end of each line)
    line = line.rstrip()

    # lowercase
    line = line.lower()  

    # extracting only letters  
    line = re.sub(r'[^a-z]', '', line)

    #looping for char
    for char in line:

        # adds it to the dict counter.
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

# ordering and printing the hours
for v, k in sorted( [ (v,k) for k, v in count.items() ], reverse=True ):
    print(k, v)
