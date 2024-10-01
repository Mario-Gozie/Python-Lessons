# -*- coding: utf-8 -*-
"""
06

Ask two numbers from the user. Print the larger one. Use if-else statement.

Example:

% python3 my_code.py 
Give first number: 3.4
Give second number: -3.4
3.4

% python3 my_code.py
Give first number: 3.4
Give second number: 1 
3.4

% python3 my_code.py
Give first number: 1
Give second number: 2
2.0
"""

first_number = float(input(f'Give first number: '))
second_number = float(input(f'Give second number: '))

if first_number > second_number:
    print(first_number)
else:
    print(second_number)


