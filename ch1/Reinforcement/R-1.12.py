# R-1.12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes
# a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.
import random


def choice(data):
    return data[random.randrange(0, len(data))]


data = [1, 2, 3, 4, 5, 6, 7, 8]
print(choice(data))
