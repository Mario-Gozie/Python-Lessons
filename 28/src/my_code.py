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


class Product:
    def __init__(self, name="", price=0.0, location="", product_code=""):
        self.name = name
        self.price = price
        self.location = location
        self.product_code = product_code

    def ask_data(self):
        self.name = input("Name: ")
        self.price = float(input("Price: "))
        self.location = input("Location: ")
        self.product_code = input("Code: ")

    def __str__(self):
        return (f"Name:       {self.name}\n"
                f"Price:      {self.price:.2f}\n"
                f"Location:   {self.location}\n"
                f"Code:       {self.product_code}")


class Cloth(Product):
    def __init__(self, name="", price=0.0, location="", product_code="", size="", material=""):
        super().__init__(name, price, location, product_code)
        self.size = size
        self.material = material

    def ask_data(self):
        super().ask_data()
        self.size = input("Size: ")
        self.material = input("Material: ")

    def __str__(self):
        return (super().__str__() + f"\nSize:       {self.size}\nMaterial:   {self.material}")


class Grocery(Product):
    def __init__(self, name="", price=0.0, location="", product_code="", country_of_origin="", best_before_date=""):
        super().__init__(name, price, location, product_code)
        self.country_of_origin = country_of_origin
        self.best_before_date = best_before_date

    def ask_data(self):
        super().ask_data()
        self.country_of_origin = input("Origin: ")
        self.best_before_date = input("Best before: ")

    def __str__(self):
        return (super().__str__() + 
                f"\nOrigin:     {self.country_of_origin}\nBest before:{self.best_before_date}")


class Appliance(Product):
    def __init__(self, name="", price=0.0, location="", product_code="", guarantee="", weight=""):
        super().__init__(name, price, location, product_code)
        self.guarantee = guarantee
        self.weight = weight

    def ask_data(self):
        super().ask_data()
        self.guarantee = input("Guarantee: ")
        self.weight = input("Weight: ")

    def __str__(self):
        return (super().__str__() + f"\nGuarantee:  {self.guarantee}\nWeight:     {self.weight}")


# Main program
if __name__ == "__main__":
    products = []

    while True:
        product_type = input("Type of product to add (1 = Groceries, 2 = Clothes, 3 = Appliance, other = quit): ").strip()
        if product_type == "1":
            product = Grocery()
        elif product_type == "2":
            product = Cloth()
        elif product_type == "3":
            product = Appliance()
        else:
            break

        product.ask_data()
        products.append(product)

    print("\nProduct details:")
    for product in products:
        print("\n" + str(product))


# if __name__ == "__main__":
#     #Main program here!
