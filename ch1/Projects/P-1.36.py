"""
P-1.36 Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however,
"""
words_map = {}
words_set = set()
words = input().split()
for word in words:
    if word in words_set:
        words_map[word] = words_map[word] + 1
    else:
        words_map[word] = 1
        words_set.add(word)

print(words_map)

"""
Mo Hello mo Mohamed Reda Mo Wow Hello Yo Yo Reda Mo

"""
