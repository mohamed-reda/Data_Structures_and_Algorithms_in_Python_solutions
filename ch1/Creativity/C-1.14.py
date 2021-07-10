# C-1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose product is odd.
def fun(data):
    for x in range(len(data)):
        for y in range(x, len(data)):
            if (x * y) % 2 == 1:
                print(f'{x} * {y} = {x * y}')


fun([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
