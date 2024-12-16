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

def main():
    # 1) Ask number of numbers to draw
    try:
        N = int(input("How many numbers? "))
        
        # Check if N is less than 1
        if N < 1:
            print("Error!")
            return
    except ValueError:
        print("Error!")
        return

    # Draw N numbers
    numbers = []
    for _ in range(N):
        # Use the specified method to draw random decimal
        random_decimal = random.randint(100, 10000) / 100
        numbers.append(random_decimal)

    # 2) Show drawn numbers
    print("Following numbers were drawn, and written to file numbers.txt:")
    print(" ".join(f"{num:.2f}" for num in numbers))

    # 3) Save numbers to file
    with open("numbers.txt", "w") as f:
        for num in numbers:
            f.write(f"{num:.2f}\n")

    # 4) Read and sort numbers
    with open("numbers.txt", "r") as f:
        sorted_numbers = sorted(float(line.strip()) for line in f)

    # 5) Print sorted numbers
    print("Following numbers were read, and sorted, from file numbers.txt:")
    print(" ".join(f"{num:.2f}" for num in sorted_numbers))

    # 6) Calculate statistics and write to results.txt
    num_count = len(sorted_numbers)
    total_sum = sum(sorted_numbers)
    average = total_sum / num_count
    min_val = min(sorted_numbers)
    max_val = max(sorted_numbers)

    # Write results to file
    with open("results.txt", "w") as f:
        f.write(f"Num: {num_count}\n")
        f.write(f"Sum: {total_sum:.2f}\n")
        f.write(f"Avg: {average:.2f}\n")
        f.write(f"Min: {min_val:.2f}\n")
        f.write(f"Max: {max_val:.2f}\n")

    # Print results
    print("\nAnd finally at file results.txt we have:")
    print(f"Num: {num_count}")
    print(f"Sum: {total_sum:.2f}")
    print(f"Avg: {average:.2f}")
    print(f"Min: {min_val:.2f}")
    print(f"Max: {max_val:.2f}")

if __name__ == "__main__":
    main()


