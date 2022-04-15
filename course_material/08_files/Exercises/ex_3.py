'''
Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.

'''

fname = input('Enter a file name: ')

try:
    fhand = open(fname)
    #fhand = open("mbox-short.txt") # comment line after debug
except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
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
        

