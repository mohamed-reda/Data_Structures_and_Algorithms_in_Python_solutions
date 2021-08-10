"""
P-1.29 Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""
l = ['c', 'a', 't', 'd', 'o', 'g']

from itertools import permutations

s = 'catdog'
for i in range(len(s)):
    for x in permutations(s, i + 1):
        print(''.join(x))

    # all_possibilities(x)
# print(6 , 5 * 6 , 5 ** 3 , 5 ** 4 , 5 ** 5)
