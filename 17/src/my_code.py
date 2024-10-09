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

################ FUNCTION FOR A LIST OF FAILED STUDENTS   ##################

def print_failed(grades):
    failed_students = []
    scores = []
    for key, value in grades.items():
        if value == 0:
            failed_students.append(key)
            scores.append(value)

    failed_result = []
    for failed_student, score in zip(failed_students, scores):
        failed_result.append(f"{failed_student} {score}")
    
    return '\n'.join(failed_result)

#######################  FUNCTION FOR COUNTING NUMBER OF FAILED STUDENTS    #######################

def failed_count(grades):
    count = 0
    for key, value in grades.items():
        if value == 0:
            count+=1
    return f"There are {count}  failed students."

################   FUNCTION FOR NAME AND GRADE COLLECTION    ######################

def ask_grades():
    Name_and_grade = {}
    while True:
        Name = input("Name: ")
        if Name == "END":
            break
        else:
            grade = input_int("Grade: ")
            if grade < 0:
                grade = 0
            elif grade > 5:
                grade = 5
            else:
                grade = grade
            Name_and_grade[Name] = grade
    return Name_and_grade

########################  FUNTION TO PRINT ALL STUDENTS    ##############################


def print_grades(grades):
    for Names, Grades in grades.items():
        if grades == 0:
            return failed_count(grades), print_failed(grades)
        else:
            return f"{Names} {Grades}"



# def ask_grades():
#     Name_and_grade = {}
#     while True:
#         Name = input("Name: ")
#         if Name == "End":
#             break
#         else:
#             grade = input("Grade: ")
#             if grade == 0 or grade < 0:
#                 grade = 0
#             elif grade == 5 or grade > 5:
#                 grade = 5
#             else:
#                 grade = grade       
            
#             Name_and_grade[Name] = grade
#     return Name_and_grade

# # print(ask_grades())

# ############## GETTING FAILED GRADES AND STUDENT

# def print_failed(grades):
#     failed_students = []
#     scores = []
#     for key, value in grades.items():
#         if value == 0:
#             failed_students.append(key)
#             scores.append(value)

#     failed_result = []
#     for failed_student, score in zip(failed_students, scores):
#         failed_result.append(f"{failed_student} {score}")
    
#     return '\n'.join(failed_result)

    



# # print(print_failed(grades=ask_grades()))

# def failed_count(grades):
#     count = 0
#     for key, value in grades.items():
#         if value == 0:
#             count+=1
#     return f"There are {count}  failed students."


# # print(failed_count(ask_grades()))

# def print_grades(grades):
#     for name, value in grades.items():
#         print(f"{name} {value}")

# print_grades(ask_grades())




###### ALL CODES HERE WORK. YOU JUST NEED TO UNDERSTAND AND FIX A SITUATION WHERE YOU HAVE TO AVOID ERROR FOR INVALID INPUTS #######

if __name__ == "__main__":
    print_grades(ask_grades())
    #Write main program below this line
    
#     def ask_grades():
#       Name_and_grade = {}
#       while True:
#         Name = input("Name: ")
#         if Name == "End":
#             break
#         else:
#           grade = input("Grade: ")
#           if grade == 0 or grade < 0:
#               grade = 0
#           elif grade == 5 or grade > 5:
#               grade = 5
#           else:
#               grade = grade       
          
#           Name_and_grade[Name] = grade
#       return Name_and_grade

#     # print(ask_grades())

# ############## GETTING FAILED GRADES AND STUDENT

#     def print_failed(grades):
#         failed_students = []
#         scores = []
#         for key, value in grades.items():
#             if value == 0:
#                 failed_students.append(key)
#                 scores.append(value)

#         failed_result = []
#         for failed_student, score in zip(failed_students, scores):
#           failed_result.append(f"{failed_student} {score}")
        
#         return '\n'.join(failed_result)

        


    
#     # print(print_failed(grades=ask_grades()))

#     def failed_count(grades):
#         count = 0
#         for key, value in grades.items():
#             if value == 0:
#                 count+=1
#         return f"There are {count}  failed students."
    

#     # print(failed_count(ask_grades()))

#     def print_grades(grades):
#         for name, value in grades.items():
#             print(f"{name} {value}")
    
#     print_grades(ask_grades())