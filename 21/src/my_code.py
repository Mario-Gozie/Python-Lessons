# -*- coding: utf-8 -*-

"""
21

1) Ask number of numbers (float) to draw, N, and draw N numbers in range 1...100 (1 and 100 included). If given N<1, then print "Error!" and terminate the software.

Use following code to draw the number:
    random_decimal = random.randint(100, 10000) / 100

2) Show the number drawn, all the numbers in same row. Separate the numbers by space.

3) Save all the numbers in file numbers.txt

4) Read all numbers from the file, and sort them from smallest to largest

5) Print the sorted numbers, all in one row.

6) Print N, mean, minimum, and maximum of the numbers, and write the same values to file results.txt

7) All float-type variables are printed/saved with 2 decimals, for example 10.10, not 10.1.

Example:
% python3 my_code.py
How many numbers? 5
Following numbers were drawn, and written to file numbers.txt:
84.32 34.41 25.22 94.88 14.45 
Following numbers were read, and sorted, from file numbers.txt:
14.45 25.22 34.41 84.32 94.88 
And finally at file results.txt we have:
Num: 5
Sum: 253.28
Avg: 50.66
Min: 14.45
Max: 94.88

The example generated file numbers.txt, containing:
84.32
34.41
25.22
94.88
14.45


In addition, the example generated, also, file results.txt, containing:
Num: 5
Sum: 253.28
Avg: 50.66
Min: 14.45
Max: 94.88
"""
import random
import statistics

##### FUNCTION TO CALCULATE PRIINT AND CALCULATE NUM, SUM, AVG, MIN, MAX

def get_Descriptive_Statistics(NumValue, Array):
     
    return f"In addition, the example generated, also, file results.txt, containing:\nNum: {NumValue}\nSum: {sum(Array):.2f}\nAvg: {statistics.mean(Array):.2f}\nMin: {min(Array)}\nMax: {max(Array)}"



# MAIN FUNCTION


def get_Number():
    while True:
        try:
            N = int(input("How many numbers: "))
        except ValueError:
            print("Error!")
        break
    random_decimal = [random.randint(100, 10000) / 100 for _ in range(N)] #### Here, I am basically saying, create a random number, do it N times and put the values in a list. The code for a longer way is below, I believe it will explain better.

    ### LONGER METHOD FOR THE RANDOM DECIMAL CODE ABOVE

    # random_decimals = []

    # # Generate 5 random decimal numbers using a traditional for loop
    # for i in range(5):
    #     random_decimal = random.randint(100, 10000) / 100
    #     random_decimals.append(random_decimal)
    with open("Numbers.txt","w") as file:
            file.write(" ".join(map(str,random_decimal)))
    print(f"Following numbers were drawn, and written to file numbers.txt:\n{' '.join(map(str,random_decimal))}")


### READING A TEXT FILE, SPLITING IT TO MAKE IT A LIST AND SORTING IT.
    with open("Numbers.txt","r") as file:
        numbers_Read = file.read()
        numbers_Read = list(map(float,numbers_Read.split()))
        numbers_Read.sort()
    print(f"Following numbers were read, and sorted, from file numbers.txt:\n{' '.join(map(str,numbers_Read))}")
    
    print(get_Descriptive_Statistics(N,numbers_Read))

get_Number()
