"""
20

Implement following functions to manage car registration data:

1) ask_cars()

- Reads registration number (key) and date of the registration (value), and saves the information information to dictionary.
- No parameters
- The function asks data until END is given as registration number.
- Date is saved as datetime.
- Input format of date is dd.mm.yyyy (for example 14.1.2023)
- If date is invalid, the software asks date again.
- Function returns the dictionary containing registration data

2) save_cars(d)

- Saves content of dictionary d to file cars.txt 
- In file, dates does not include time information
- Each row contains registration number and registration date separated by tabulator '\t'

3) read_cars()

- Reads registration data from cars.txt, and returns a dictionary containing registration data saved.

4) print_data(d)

- Prints registration data saved on dictionary d.


NOTE: If you utilize

for row in f:
   ...

to read the file, then row contains new line, also. You can use str.strip() to remove new line.

Create test software to test your solution, if needed.

Example:
% python3 my_code.py
Registration number : A-13
Registration date: 1.3.1923
Registration number : B-334
Registration date: 12.3.1945
Registration number : AAA-111
Registration date: 123.2.1928
Error: Give date in format dd.mm.yyyy : 12.3.1928
Registration number : END
A-13 01.03.1923
B-334 12.03.1945
AAA-111 12.03.1928

In addition, the test program created cars.txt file containing:
A-13    01.03.1923
B-334   12.03.1945
AAA-111 12.03.1928
"""
#Write functions, define global variables, and import modules here!

from datetime import datetime

car_reg_dict = {}


def ask_car():
   while True:
      Registeration_number = input("Registeration number: ")
   
      if Registeration_number == "END":
         break
      else:
         while True:
            Registeration_date = input("Registeration Date (DD.MM.YYYY): ")

               # Convert the user input to a date
            try:
               user_date_time = datetime.strptime(Registeration_date, "%d.%m.%Y")
               user_date = user_date_time.strftime("%d.%m.%Y")
               car_reg_dict[Registeration_number] = user_date
               break
            except ValueError:
               print(f'Error: Give date in format dd.mm.yyyy : 12.3.1928')
               pass
   return car_reg_dict         




###################### FUNCTION FOR WRITING CAR REGISTERATION DETAILS INTO A TEXT FILE

def save_car(dict):
   #### Opening of file called "cars.txt" in append mode "a" instead of write mode "w". which means, I don't want to overwrite the file or create a new one if it does not exist. I just want to add new values to the existing file.
   with open("cars.txt", "a") as file:
   ## The with block here helps to close the file automatically when the with block ends.


   #### Iterating over the dictionary
      for RegNo, RegDate in dict.items():
         ### writing each registeration number and date to the file.
         ### Seperate the values by a tab "\t" and end the line with a new line "\n"
         file.write(f"{RegNo}\t{RegDate}\n")



######    FUNCTION FOR GETTING A DICTIONARY OF REGISTERATI0N NUMBER AND DATE FROM A TEXT FILE 

def read_cars():

   Car_reg_dict_from_file = {}

   # Opening file in read mode. remember that the read staement will close the file after the block code
   with open("cars.txt","r") as file:
      for line in file:
         # The Strip removes any leading or trailing whitespace and split by tab (\t)
         parts = line.strip().split("\t")

         if len(parts) == 2:
            RegNo, Date = parts
            Car_reg_dict_from_file[RegNo] = Date
   return Car_reg_dict_from_file



##### THE FUNCTION THAT PRINTS RESULT AFTER ALL THE ACTION

def print_data(x):
   save_car(x)
   car_fr_file = read_cars()
   print("In addition, the test program created cars.txt file containing:")
   for reg_no, date in car_fr_file.items():
      print(f"{reg_no} {date}")
   

if __name__ == "__main__":
    #Write main program below this line

   print_data(ask_car()) 


