'''
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

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

def computepay(hours, rate):

    if hours <= max_hours:
        pay = hours * rate
    else:
        extra_hours = hours - max_hours

        pay = ( max_hours * rate ) + ( extra_hours * rate * 1.5 )
    return pay

print(f'Pay: {computepay(hours, rate)}')