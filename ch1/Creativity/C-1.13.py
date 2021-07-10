# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def reverse(data):
    for i in range(int(len(data) / 2)):
        data[i], data[len(data) - i - 1] = data[len(data) - i - 1], data[i]
    return data


l = reverse(l)
print(l)
