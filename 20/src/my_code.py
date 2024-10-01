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

if __name__ == "__main__":
    #Write main program below this line

    


