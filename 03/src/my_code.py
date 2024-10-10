# -*- coding: utf-8 -*-

"""
03

Ask user two integer values into two variables named as first_value and 
second_value.

Output:
- first_value+second_value
- first_value-second_value
- first_value*second_value

Each value shall be printed on separate row. Below is an eaxample:

Give 1st number: 10
Give 2nd number: 5
Sum:        10 + 5 = 15
Difference: 10 - 5 = 5
Product:    10 * 5 = 50
"""

first_value = int(input("Give 1st number: "))
second_value = int(input("Give 2nd number: "))
print (f"Sum:         {first_value} + {second_value} = {first_value + second_value}")
print (f"Difference:  {first_value} - {second_value} = {first_value - second_value}")
print (f"Product:     {first_value} * {second_value} = {first_value * second_value}")




