"""
28

You task is to design classes to store products of a department store.

1) All producs (class Product) share common properties:
  - name
  - price
  - location
  - product_code

2) Clothes (class Cloth) contains following additional properties:
  - size
  - material

3) Groceries (class Grocery) contains following additional properties:
  - country_of_origin
  - best_before_date

4) Household appliances (class Appliance) contains following additional properties:
  - guarantee
  - weight

5) Each class contains a method ask_data which asks product data from the user

6) Create a software that asks products from the user. Before terminating, the software prints data. See example: 


Type of product to add (1 = Groceries, 2 = Clothes, 3 = Appliance, other = quit: 1
Name: Sugar
Price: 2.3
Location: groceries 2345
Code: 728634
Origin: Finland
Best before: 2027

Type of product to add (1 = Groceries, 2 = Clothes, 3 = Appliance, other = quit: 1
Name: Beef
Price: 12.8
Location: fridge 12
Code: a37373
Origin: Denmark
Best before: 1.9.2023

Type of product to add (1 = Groceries, 2 = Clothes, 3 = Appliance, other = quit: 2
Name: T-shirt
Price: 21.10
Location: clothes 11
Code: 293874s
Size: M
Material: Cotton                

Type of product to add (1 = Groceries, 2 = Clothes, 3 = Appliance, other = quit: 3
Name: Fridge
Price: 490
Location: Warehouse A
Code: 48375
Guarantee: 5 years
Weight: 35kg

Type of product to add (1 = Groceries, 2 = Clothes, 3 = Appliance, other = quit: x

Name:       Sugar
Price:      2.30
Location:   groceries 2345
Code:       728634
Origin:     Finland
Best before:2027

Name:       Beef
Price:      12.80
Location:   fridge 12
Code:       a37373
Origin:     Denmark
Best before:1.9.2023

Name:       T-shirt
Price:      21.10
Location:   clothes 11
Code:       293874s
Size:       M
Material:   Cotton

Name:       Fridge
Price:      490.00
Location:   Warehouse A
Code:       48375
Guarantee:  5 years
Weight:     35kg
"""

from datetime import datetime
#Write class and imports here!


if __name__ == "__main__":
    #Main program here!
