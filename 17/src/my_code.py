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



def input_integer(msg):
    """
    Prompts the user for an integer repeatedly until a valid input is provided.

    Args:
        msg: The prompt message to display to the user.

    Returns:
        The integer entered by the user.
    """
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Please enter a valid integer.")

def ask_grades():
    """
    Prompts the user to enter student names and grades.

    Returns:
        A dictionary containing student names as keys and their corresponding grades as values.
    """
    grades = {}
    while True:
        name = input("Name: ")
        if name == "END":
            break
        grade = input_integer("Grade: ")
        grade = max(0, min(grade, 5))  # Clamp grade to 0-5
        grades[name] = grade
    return grades

def failed_count(grades):
    """
    Counts the number of students who failed (grade 0).

    Args:
        grades: A dictionary of student names and their grades.

    Returns:
        The number of failed students.
    """
    return sum(1 for grade in grades.values() if grade == 0)

def print_failed(grades):
    """
    Prints the names and grades of failed students.

    Args:
        grades: A dictionary of student names and their grades.
    """
    print(f"There are {failed_count(grades)} failed students.")
    for name, grade in grades.items():
        if grade == 0:
            print(name, grade)

def print_grades(grades):
    """
    Prints the names and grades of all students.

    Args:
        grades: A dictionary of student names and their grades.
    """
    for name, grade in grades.items():
        print(name, grade)

if __name__ == "__main__":
    grades = ask_grades()
    if failed_count(grades) > 0:
        print_failed(grades)
    else:
        print_grades(grades)