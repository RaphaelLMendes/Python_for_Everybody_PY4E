
'''
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

'''


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