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


def make_change(given, charged, denominations=[100, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]):
    assert given >= charged, 'The customer has not given enough!'
    change = {}
    residual = given - charged
    for denomination in denominations:
        amount, residual = divmod(residual, denomination)
        if amount: change[denomination] = int(amount)  # This will only add non-zero amounts to the dictionary
    return change


def make_change_2(given, charged, denominations=[100, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]):
    assert given >= charged, 'The customer has not given enough!'
    change = {}
    residual = given - charged
    print(f'residual = {residual}')
    for denomination in denominations:
        amount, residual = divmod(residual, denomination)

        if amount:
            change[denomination] = int(amount)  # This will only add non-zero amounts to the dictionary
    return change


# print(make_change(1000, 575))
# print(make_change(1000.84, 575))
print(make_change_2(1000, 575))
print(425 / 100)
# print(1000 - 575)
print(425 % 100)
# print(make_change_2(1000.84, 575))
