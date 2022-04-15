'''
Exercise 1: 

Write a program which repeatedly reads numbers until the 
user enters “done”. Once “done” is entered, print out the 
total, count, and average of the numbers. If the user 
enters anything other than a number, detect their mistake 
using try and except and print an error message and skip 
to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333

'''

numbers = []

while True:
    num_input = input('Enter a number: ')
    
    if num_input == "done":
        break

    try:
        number = float(num_input)
        numbers.append(number)
    except:
        print('Invalid input!')
        continue

def total(list):
    number = 0
    for num in list:
        number+=num
    return number

print(total(numbers), len(numbers), total(numbers)/len(numbers))
