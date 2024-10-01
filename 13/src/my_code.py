# -*- coding: utf-8 -*-


"""
13

1) Create an empty list named as numbers
2) Read 5 integers from the user, and insert them to numbers list
3) Print sum of the integers
4) Print average of the integers with 3 digits after decimal point
5) Print the numbers space separated, all in one row

Example:

% python3 my_code.py
Give a number: 1
Give a number: 0
Give a number: -5
Give a number: 3
Give a number: -66
Sum is: -67
Average is : -13.400
Numbers: 1 0 -5 3 -66 


"""

numbers = []
Total_of_Array = 0
Average = 0

def get_array():
    
    counter = 0
    while True:
        user_number = int(input(f"Give a number: "))
        numbers.append(user_number)
        counter += 1
        if counter == 5:
            break
    return f'Sum is: {sum(numbers)}\nAverage is: {(sum(numbers)/len(numbers)):.3f}\nNumbers: {" ".join(map(str, numbers))}'

print(get_array())
