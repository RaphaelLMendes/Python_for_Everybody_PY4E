'''
Exercise 2: 

Write a program that categorizes each mail message by which day of the week the commit was done. 
To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
At the end of the program print out the contents of your dictionary (order does not matter).

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
    if(line.startswith('from')):

        # In thist case i used a try and except to get away with grabing only the lines with dates, but generally except blocks with a pass is not "good" code.
        # It makes you less in controll of your code. Especially if it doesnt have a traceback. 
        # You should be in controll of every possibility that may ocurr in your code in real apps.
        try:

            #grabs the third word
            date = line.split(' ')[2]
            #print(date)

            #adds it to the dict counter.
            if date not in count:
                count[date] = 1
            else:
                count[date] += 1
        except:
            pass
            #print(' this line doesnt have a date.')

# prints out our dict
print(count)
