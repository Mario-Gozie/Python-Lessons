"""
19

Create a function named check, which gets arbitrary number of arguments:
1) At first, the function prints number of arguments got.
2) If there are none parameters the function prints "Error!" and terminates
3) If the 1st argument is "teacher" the function prints "Teaching programming!"
4) If the 1st argument is "student" the function prints "Learning programming!"
5) If the 1st parameter is not "teacher" nor "student" the function prints "I don't understand!"
"""
#Write functions and define global variables here!

def check(*agr):
    print(f"Number of arguments: {len(agr)}")
    if len(agr) == 0:
        print("Error!")
        return
    if agr[0] == "teacher":
        print("Teaching Programming")
    elif agr[0] == "student":
        print("Learining programming")
    else:
        print("I don't understand")


if __name__ == "__main__":
    check()
    #Write main program below this line
    pass
