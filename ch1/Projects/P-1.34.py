"""
P-1.34 A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""
import random

sentence = "I will never spam my friends again."

randomList = set()
current = 0
while len(randomList) < 8:
    randomList.add(int(random.random() * 100))

randomList = list(randomList)
randomList.sort()
print(randomList)
for i in range(100):
    sentence = "I will never spam my friends again."
    if current < 8 and randomList[current] == i:
        sentence += " <== typos"
        current += 1
        # print(current)
    print(sentence)
