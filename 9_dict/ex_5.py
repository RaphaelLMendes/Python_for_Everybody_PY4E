'''
Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from 
(i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

'''

# defining file to be used ( this can be an input value )
file = 'files\mbox-short.txt'

# opening the file and creating a handler object
fhand = open(file, 'r')

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
        domain = line.split(' ')[1].split("@")[1]
        #print(domain)

        # adds it to the dict counter.
        if domain not in count:
            count[domain] = 1
        else:
            count[domain] += 1


print(count)