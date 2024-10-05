# -*- coding: utf-8 -*-

"""
12


Suplementary benefit is a fiacial benefit for people with low income. Create a software that computes amount of the benefit for a single person for a given number of days.

Basis amount of the benefit:
16.18€ for a solitaire
17.80€ for a solitare with children
13.76€ for cohabit (each one)

The amount is increased by:
11.33€ by each children age 10-17 years
10.20€ by each childres age less than 10

The software ask information in order defined by the example.

Finally the software prints amount of the benefita and asks if the user wants to compute amount of the benefit with different data.

Example:
% python3 my_code.py
New data (y/n): y
Solitaire (1) or cohabit (2): 1
Any underage children (y/n): y
Children less than 10 years: 2
Children 10-17 years: 0
Days: 10
Amount of the benefit is 382.00 euro
New data (y/n): y
Solitaire (1) or cohabit (2): 1
Any underage children (y/n): n
Days: 10
Amount of the benefit is 161.80 euro
New data (y/n): y
Solitaire (1) or cohabit (2): 2
Any underage children (y/n): y
Children less than 10 years: 0
Children 10-17 years: 1
Days: 10
Amount of the benefit is 250.90 euro
New data (y/n): y
Solitaire (1) or cohabit (2): 2
Any underage children (y/n): n
Days: 10
Amount of the benefit is 137.60 euro
New data (y/n): n
"""

#########################  VARIABLES   ##########################

solitare = 16.18
single_parent = 17.80
cohabit = 13.76

Teenagers = 11.33
children = 10.20

###############################   MODIFICATION STARTS    ###############################

####################    FUNCTION FOR CHILDREN BENEFITS     ###############################
def based_on_children():
    Children_no = int(input(f"Children less than 10 years: "))
    Total_Children = Children_no * children
    Teenagers_no = int(input(f"Children 10-17 years: "))
    Total_Teenagers = Teenagers * Teenagers_no
    return Total_Teenagers + Total_Children

######################  CALCULATION FOR THE BENEFITS  BASED ON STATUS  #########################

def based_on_status():
    new_data = input("New data (y/n): ")
    if new_data == 'y':
        marital_satus = int(input("Solitaire (1) or cohabit (2): "))
        if marital_satus == 1:
            underaged = input("Any underage children (y/n):  ")
            if underaged == 'y':
                return based_on_children() + single_parent
            elif underaged == 'n':
                return solitare
        elif marital_satus == 2:
            underaged = input("Any underage children (y/n):  ")
            if underaged == 'y':
                return based_on_children() + cohabit
            elif underaged == 'n':
                return cohabit


######################       CALCULATION FOR DAYS     #############################

def No_of_days():
    Days = int(input(f"Days: "))
    return Days


#######################    FINAL BENEFIT CALCULATION       #########################

def Calculate_benefit():
    Total_benefit = (based_on_status()* No_of_days())
    
    return (f"Amount of the benefit is {Total_benefit:.2f} euro")


#############################  CALLING THE FINAL FUNCTION    ##########################
    
print(Calculate_benefit())



################ BEFORE MODIFICATION ############################

# def based_on_status():
#     new_data = input("New data (y/n): ")
#     if new_data == 'y':
#         marital_satus = int(input("Solitaire (1) or cohabit (2): "))
#         if marital_satus == 1:
#             underaged = input("Any underage children (y/n):  ")
#             if underaged == 'y':
#                 Children_no = int(input(f"Children less than 10 years: "))
#                 Total_Children = Children_no * children
#                 Teenagers_no = int(input(f"Children 10-17 years: "))
#                 Total_Teenagers = Teenagers * Teenagers_no
#                 return Total_Teenagers + Total_Children + single_parent
#             elif underaged == 'n':
#                 return solitare
#         elif marital_satus == 2:
#             underaged = input("Any underage children (y/n):  ")
#             if underaged == 'y':
#                 Children_no = int(input(f"Children less than 10 years: "))
#                 Total_Children = Children_no * children
#                 Teenagers_no = int(input(f"Children 10-17 years: "))
#                 Total_Teenagers = Teenagers * Teenagers_no
#                 return Total_Teenagers + Total_Children + cohabit
#             elif underaged == 'n':
#                 return cohabit
    
# def No_of_days():
#     Days = int(input(f"Days: "))
#     return Days



# def Calculate_benefit():
#     Total_benefit = (based_on_status()* No_of_days())
    
#     return (f"Amount of the benefit is {Total_benefit:.2f} euro")

    
# print(Calculate_benefit())
