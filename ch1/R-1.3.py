# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

userData = input().split()


def min_max(data):
    maxNumber = int(data[0])
    minNumber = int(data[0])
    for index in range(len(data)):
        data[index] = int(data[index])
        if data[index] > maxNumber:
            maxNumber = data[index]
        if data[index] < minNumber:
            minNumber = data[index]
    return minNumber, maxNumber


print(min_max(userData))

# try
# 2 3 56 7 8 9
