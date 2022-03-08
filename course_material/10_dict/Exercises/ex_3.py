'''
Exercise 3: 
Write a program to read through a mail log, build a histogram using a dictionary to count how many messages 
have come from each email address, and print the dictionary.

'''
# opening the file and creating a handler object
fhand = open('files\mbox-short.txt', 'r')

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


# prints out our dict
print(count)