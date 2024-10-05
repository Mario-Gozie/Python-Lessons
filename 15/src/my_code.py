# -*- coding: utf-8 -*-

"""
15

1) Ask language to use.
  - 0=Finnish
  - 1=English
  - Default is Finnish -> If answer is not 0 or 1 Finnish will be used

2) Days of week in Finnish are: maanantai (=Monday), tiista, keskiviikko, torstai, perjantai, lauantai, and, sunnuntai (=Sunday)

3) Create a list containing days of week starting from Monday in both languages

4) Create a dictionary, where you store 4 measurements of amount of rain on each day between Monday and Friday.

5) Ask measurement data from the user, and fill dictionary

6) Finally, print average amount of the rain on each day 


Example:

Please choose language (0 = suomi, 1 = english): 1
Monday 1. : 3
Monday 2. : 2
Monday 3. : 4
... Cut rows ...
Friday 2. : 6
Friday 3. : 5
Friday 4. : 3

Monday 3.5 mm
Tuesday 3.2 mm
Wednesday 4.0 mm
Thursday 4.2 mm
Friday 4.8 mm
"""

Finnish = ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"]

English = ["Monday","Tuesday","wednesday","Thursday","Friday", "Saturday", "Sunday"]

temp_values = {}

language = input("Please choose language (0 = suomi, 1 = english): ")

if language == "1":
  for days in English:
    for i in range(5):  #This loop will loop through numbers between 1 to 5 which is from 1 to 4. five is not included
      temp_values[f"{days} {i}"] = float(input(f"{days} {i}: ")) #Now, it will produce each day 4 times and number 1 to 4 by it's side.
      
else:
  for days in Finnish:
    for i in range(5):  #This loop will loop through numbers between 1 to 5 which is from 1 to 4. five is not included
      temp_values[f"{days} {i}"] = float(input(f"{days} {i}: ")) #Now, it will produce each day 4 times and number 1 to 4 by it's side.

grouped_days = {}  # dictionary that will carry average values for the week 

for key, value in temp_values.items(): ## iterating the original dictionary to create one day name instead of "Monday 1", Monday 2, Tuesday 1, Tuesday 2 etc.
  day = key.split()[0]
  if day not in grouped_days:
    grouped_days[day] = [] #Here I am creating a key for each day within the dictionary that will carry average values for the week
  grouped_days.setdefault(day,[]).append(value) # To append to a list, you need to set the key of the dictionary to a default of list.

for key, value in grouped_days.items():
  print(f'{key} {(sum(value)/len(value)):.1f} mm')



















#####################    FIRST SET OF CODE    #################3



# Finnish = ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"]

# English = ["Monday","Tuesday","wednesday","Thursday","Friday", "Saturday", "Sunday"]

# temp_values = {}

# language = input("Please choose language (0 = suomi, 1 = english): ")

# if language == "1":
#   for days in English:
#     for i in range(1,5):  #This loop will loop through numbers between 1 to 5 which is from 1 to 4. five is not included
#       temp_values[f"{days} {i}"] = float(input(f"{days} {i}: ")) #Now, it will produce each day 4 times and number 1 to 4 by it's side.
      
# else:
#   for days in Finnish:
#           for i in range(1,5):  #This loop will loop through numbers between 1 to 5 which is from 1 to 4. five is not included
#             temp_values[f"{days} {i}"] = float(input(f"{days} {i}: ")) #Now, it will produce each day 4 times and number 1 to 4 by it's side.

# print(temp_values)
  

