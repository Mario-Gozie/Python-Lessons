"""
16

1) Create function AskAndTest, which asks an integer from the user.
   The function returns
   * 1, if the integer was positive
   * 0, if the integert was 0
   * -1, if the integer was negative

2) Create a main program that utilizes AskAndTest function. The main program
   prints message "Positive", "Zero", or "Negative" corresponding return
   value of the function.

Example:
 % python3 my_code.py
Give an integer: 21
Positive

% python3 my_code.py
Give an integer: 1
Positive

% python3 my_code.py
Give an integer: 0
Zero

% python3 my_code.py
Give an integer: -1
Negative

% python3 my_code.py
Give an integer: -100
Negative
"""

######   Implement AskAndTest function here!
def AskAndTest():
   integer = int(input('Give an integer:  '))
   if integer < 0:
      return -1
      
   elif integer > 0:
      return 1
      
   elif integer == 0:
      return 0
      
#####  A FUNCTION THAT PRINTS EVALUATION RESULT.

def message():
   x = AskAndTest()
   if x == 1:
      print('Positive')
   elif x == -1:
      print('Negative')
   elif x == 0:
      print("Zero")





if __name__ == "__main__":
    #Write main program below this line
   
   message()




