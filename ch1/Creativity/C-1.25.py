"""
C-1.25 Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
"""


def fun(s):
    # vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    n = ''
    for x in range(len(s)):
        if s[x].isalpha() or s[x] == ' ':
            n += s[x]
    return n


print(fun('Lets try, Mike.'))
