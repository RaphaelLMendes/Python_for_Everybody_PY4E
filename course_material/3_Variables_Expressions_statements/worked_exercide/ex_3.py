'''
Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
'''

hours = input('Hours: ')
rate = input('Rate: ')

pay = int(hours) * float(rate)

print(f'Your pay is: {pay}')