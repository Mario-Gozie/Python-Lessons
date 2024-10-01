"""
17

1) The software asks gredes, 0-5, of students participating basics of programming course. Use input_integer function to read an integer from the user.
2) Feeding of grades ends when END is given as name.
3) If given grade is less than 0, the grade is set as 0.
4) If given grade is greater than 5, the grage is set as 5.
5) Use dictionary, with key=name and value=grade, to store grades.
6) You may assume that there are no two students with same name.
7) If there are failed students, grade=0, the software prints number of failed students and name of failed students.
8) If there are no failed students, then software prints all grades with names.
9) Implement following functions:
  - ask_grades() - Asks names and grades of all students.
    Returns a dictionary containing grades and names.

  - print_failed(grades) - Prints failed student names.
    grades=the dictionary containing grades.

  - failed_count(grades) - Return number of failed students.

  - print_grades(grades) - Print all students and grades.
10) Make sure that the software do not crash if invalid input is given.

Example without failed students (Note: Kaisa's grade have been converted 6->5):
% python3 my_code.py
Name : Janne
Grade : 1
Name : Matti
Grade : 4
Name : Kaisa
Grade : 6
Name : END
Janne 1
Matti 4
Kaisa 5


Example with failed students and bad input (Note: Janne's grade have been converted -1->0):
% python3 my_code.py
Name : Janne
Grade : -1
Name : Matti
Grade : 0
Name : Kaisa
Grade : 5
Name : Bad Input
Grade : A 
Grade : 5
Name : END
There are 2  failed students.
Janne 0
Matti 0


"""

#Call this  function to read integer from the user
#Reads an integer from the keyboard and shows msg.
#If given string is not valid integer a new one will be asked
def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except:
            pass



#Write your functions here!



if __name__ == "__main__":
    #Write main program below this line

        
