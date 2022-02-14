'''
Exercise 4: 
Add code to the above program to figure out who has the most messages in the file. 
After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop 
(see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

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


# Now we have to reverse the dict so that we can aply a max() function and get the key.
print(max(count, key=count.get)+" "+str(count[max(count, key=count.get)]))