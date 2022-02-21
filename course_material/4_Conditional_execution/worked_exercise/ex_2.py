'''
Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input 
gracefully by printing a message and exiting the program. The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
'''

#Already did this in EX 1

hours = input('Enter Hours: ')

try:
    hours = float(hours)
except:
    raise TypeError("value typed needs to be a number")

rate = input('Enter Rate: ')

try:
    rate = float(rate)
except:
    raise TypeError("value typed needs to be a number")


max_hours = 40

if hours <= max_hours:
    pay = hours * rate
else:
    extra_hours = hours - max_hours

    pay = ( max_hours * rate ) + ( extra_hours * rate * 1.5 )

print(f'Pay: {pay}')