"""
C-1.27 In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementations,
from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance advantages.
"""


def factors(n):  # traditional function that computes factors
    results = []  # store factors in a new list
    for k in range(n):
        if n % (n - k) == 0:  # divides evenly, thus k is a factor
            results.append(n - k)  # add k to the list of factors
    return results  # return the entire list


print(factors(10))
