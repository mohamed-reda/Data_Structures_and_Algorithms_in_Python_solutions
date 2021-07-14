"""
C-1.20 Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""

import random

data = [random.randint(0, i) for i in range(10)]
random.shuffle(data)
print(data)
