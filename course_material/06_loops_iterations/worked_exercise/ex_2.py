''' 

Exercise 2: Write another program that prompts for a list 
of numbers as above and at the end prints out both the 
maximum and minimum of the numbers instead of the average.

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

def max_min(list):
    Max_number = list[0]
    min_number = list[0]
    for num in list:
        if num > Max_number:
            Max_number=num
        if num < min_number:
            min_number=num
    return Max_number, min_number

max_num, min_num = max_min(numbers)

print(max_num, min_num)
