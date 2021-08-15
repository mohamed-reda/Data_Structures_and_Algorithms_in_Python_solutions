"""
P-1.30 Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""

# --------P1-30
import math


# Apporach 1: Using the log function
def find_log2(number):
    assert number > 2, 'The number should be greater than 2'
    return int(math.log(number, 2) // 1)


# Approach 2: A while loop
def find_num_divide_2(number):
    divides = 0
    while number >= 2:
        divides += 1
        number /= 2
    return (divides)


print('Approach 1')
for x in range(3, 100):
    print(find_log2(x), end=', ')

print('\n\nApproach 2')
for x in range(3, 100):
    print(f'x = {x} and {find_num_divide_2(x)}, ')

# print(f'x = {10} and {find_num_divide_2(10)}, \n')
