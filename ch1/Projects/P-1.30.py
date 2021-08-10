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
    print(find_num_divide_2(x), end=', ')
"""
P-1.31 Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""

"""
P-1.32 Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""

"""
P-1.33 Write a Python program that simulates a handheld calculator. Your program
should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each operation
is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
"""

"""
P-1.34 A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""

"""
P-1.35 The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.
"""

"""
P-1.36 Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however,
"""
