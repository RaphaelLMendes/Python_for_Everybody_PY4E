'''
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

Test your file on the mbox.txt and mbox-short.txt files.

'''

fname = input('Enter a file name: ')

try:
    fhand = open(fname)
    #fhand = open("mbox-short.txt") # comment line after debug
except:
    print(f'file not found: {fname}')
    quit()

values = []

for line in fhand:
    line = line.rstrip()
    if line.upper().startswith("X-DSPAM-CONFIDENCE:"):
        value = float(line.upper()[20:])
        values.append(value)

def calculate_average(list_of_values):
    if len(list_of_values)<1:
        return(0)
    sum = 0
    for value in list_of_values:
        sum += value
    
    return sum/len(list_of_values)

print(f'Average spam confidence: {calculate_average(values)}')
        

