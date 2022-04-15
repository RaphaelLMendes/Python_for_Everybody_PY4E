'''
Exercise 5: Write a program which prompts the user for a Celsius temperature, 
convert the temperature to Fahrenheit, and print out the converted temperature.
'''

# The Formula for the conversion is degrees Celsius times 9 divided by 5 plus 32

cel = input('Celsius temperature: ')

far = float(cel) * 9 /5 + 32

print(f'Fahrenheit temperature: {far}')

