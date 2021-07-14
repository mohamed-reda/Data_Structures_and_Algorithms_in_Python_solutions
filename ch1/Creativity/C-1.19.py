# C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.
print(ord('a'))
print(ord('z'))
print(chr(97))
print([chr(x) for x in range(97, 123)])
