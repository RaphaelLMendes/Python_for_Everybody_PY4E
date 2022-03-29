'''
Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
You can pull the hour from the “From” line by finding the time string and then splitting that string 
into parts using the colon character. Once you have accumulated the counts for each hour, print out 
the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

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

        #print(line.split(' '))

        #grabs the time
        time = line.split(' ')[6]

        #grabs the hour
        hour = time.split(':')[0]

        

        # adds it to the dict counter.
        if hour not in count:
            count[hour] = 1
        else:
            count[hour] += 1

# ordering and printing the hours
for k, v in sorted( [ (k,v) for k, v in count.items() ] ):
    print(k, v)
