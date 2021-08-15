"""
P-1.32 Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""


def the_sum(i, ii):
    return i + ii


def the_subtract(i, ii):
    return i - ii


def the_multiplication(i, ii):
    return i * ii


def the_division(i, ii):
    if ii == 0:
        return "You can't divide into 0"
    return i / ii


first = float(input())
operation = input()
second = float(input())

d = {'+': the_sum(first, second), '-': the_subtract(first, second), '*': the_multiplication(first, second),
     '/': the_division(first, second), }
print(d[operation])
