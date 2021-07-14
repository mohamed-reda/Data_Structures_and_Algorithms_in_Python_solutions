"""
C-1.26 Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
"""
l = []
for i in range(3):
    l.append(int(input()))
if l[0] + l[1] == l[2]:
    print('a + b = c')

if l[0] == l[1] - l[2]:
    print('a = b−c')

if l[0] * l[1] == l[2]:
    print('a ∗ b = c')
