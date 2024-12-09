# -*- coding: utf-8 -*-

"""
11

Main menu of the software looks like:

0 = Exit
1 = Give radius
2 = Compute circumference of the circle
3 = Compute area of the circle

- Default radius is 0.
- 0 terminates the software
- 1 asks radius from the user
- 2 prints circumference of the circle with given radius
- 3 prints area of the circle with given radius
- Other than 0, 1, 2, or 3 terminates the software
- After 1, 2, or 3 the menu is printed again
- Print all non-integers with 2 digits after decimal point
- Use math.pi as pi

Example:

% python3 my_code.py


0 = Exit
1 = Give radius
2 = Compute circumference of the circle
3 = Compute area of the circle
Select: 1
Give radius: 2.1


0 = Exit
1 = Give radius
2 = Compute circumference of the circle
3 = Compute area of the circle
Select: 2
Circumference is 13.19


0 = Exit
1 = Give radius
2 = Compute circumference of the circle
3 = Compute area of the circle
Select: 3
Area is 13.85


0 = Exit
1 = Give radius
2 = Compute circumference of the circle
3 = Compute area of the circle
Select: 0
"""


from math import pi

radius = 0



def software():
    print("Main menu of the software looks like: \n\n0 = Exit \n1 = Give radius \n2 = Compute circumference of the circle \n3 = Compute area of the circle")


def get_area(radius):
    return pi*radius**2

def get_circumference(radius):
    return 2*pi*radius



while True:
    software()
    select = float(input('SELECT: '))
    if select == 1:
        radius = float(input("Give radius: "))
        print(radius)
    elif select == 2: 
        circumference = get_circumference(radius)
        print(f"Circumference is {circumference: 2f}")  
    elif select == 3:
        area = get_area(radius)
        print(f"Area is {area: 2f}")
    else:
         break
    


