'''
Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195

'''

# opening the file and creating a handler object
fhand = open('../../files/mbox-short.txt', 'r')

# creating the disctionairy to be able to count occurrences
count = {}

# loop through each line in the file
for line in fhand:

    # removing whitespaces ( \n at the end of each line)
    line = line.rstrip()
    line = line.lower()

    # checking if it is the line with the info I want.
    if(line.startswith('from') and len(line.split(' '))>2):


        #grabs the third word
        sender = line.split(' ')[1]
        #print(sender)

        # adds it to the dict counter.
        if sender not in count:
            count[sender] = 1
        else:
            count[sender] += 1

most_common = sorted([ (v, k) for k,v in count.items() ], reverse=True)

for v, k in most_common[:1]:
    print(k, v)
    
#print(most_common[0][1], most_common[0][0])