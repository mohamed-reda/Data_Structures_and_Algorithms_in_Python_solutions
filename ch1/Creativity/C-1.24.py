"""
C-1.24 Write a short Python function that counts the number of vowels in a given
character string.
"""


# def find vowles():

def find_vowels(s):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    n = 0
    for x in s:
        if x in vowels:
            n += 1
    return n


print(find_vowels('Lets try, Mike.'))
