# """
# 23

# Implement two lambda functions:

# - summation: Takes 2 parameters, x and y, and returns x+y
# - multiplication: Takes 2 parameters, x and y, and returns x*y

# In addition, create compute(f, numbers) function.
# - f is either summation or multiplication.
# - numbers is a list containing numbers fetch to f.
# - numbers may contain 0...N numbers.
# - If numbers is empty, then compute returns 0.
# - If numbers contains more than 2 numbers you can utilize recursion:
#   For example, if numbers=[1, 2, 3] then compute returns summation(summation(1, 2), 3) etc.

# Main program is implemented below, don't modify it.

# Example:
# % python3 my_code.py
# 1320
# 28
# 4
# 4
# 0
# 0

# """
# #Write lambdas and laske here

# summation = lambda x,y: x+y#Insert your code here  
# multiplication = lambda x,y: x*y#Insert your code here

# print(summation(2,3))
# print(multiplication(2,3))



# def compute(f, numbers):
    
#     #Your code here
    
#     return result


# #Don't touche lines below
# if __name__ == "__main__":
#     numbers = [1,5,8,11,3]
#     print(compute(multiplication, numbers))
#     print(compute(summation, numbers))

#     numbers = [4]
#     print(compute(multiplication, numbers))
#     print(compute(summation, numbers))

#     numbers = []
#     print(compute(multiplication, numbers))
#     print(compute(summation, numbers))

# Define the lambda functions for summation and multiplication
summation = lambda x, y: x + y
multiplication = lambda x, y: x * y

# Define the compute function with recursive handling
def compute(f, numbers):
    if not numbers:          # If list is empty, return 0
        return 0
    elif len(numbers) == 1:   # If list has only one element, return it
        return numbers[0]
    else:
        # Recursively apply function f to the first element and the result of the rest
        return f(numbers[0], compute(f, numbers[1:]))

# Don't touch lines below
if __name__ == "__main__":
    numbers = [1, 5, 8, 11, 3]
    print(compute(multiplication, numbers))  # Output: 1320
    print(compute(summation, numbers))       # Output: 28

    numbers = [4]
    print(compute(multiplication, numbers))  # Output: 4
    print(compute(summation, numbers))       # Output: 4

    numbers = []
    print(compute(multiplication, numbers))  # Output: 0
    print(compute(summation, numbers))       # Output: 0
