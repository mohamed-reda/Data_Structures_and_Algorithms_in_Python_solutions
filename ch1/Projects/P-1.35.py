"""
P-1.35 The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.
"""
import random


def test_birthday_paradox(num_people):
    birthdays = [random.randrange(0, 365) for _ in range(num_people)]
    birthday_set = set()
    for bday in birthdays:
        if bday in birthday_set:
            return True
        else:
            birthday_set.add(bday)
    return False


def paradox_stats(num_people=23, num_trials=100):
    num_successes = 0
    for _ in range(num_trials):
        if test_birthday_paradox(num_people): num_successes += 1
    return num_successes / num_trials


for x in range(101):
    print(f'For {x} people, the probability is approximately: {paradox_stats(x)}')

print(f'For {24} people, the probability is approximately: {paradox_stats(24)}')
