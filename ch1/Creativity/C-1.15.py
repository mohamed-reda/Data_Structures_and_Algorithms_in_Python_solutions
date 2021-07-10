# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).


def fun(data):
    list.sort(data)
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            print('you have 2 numbers equal each other')
            return
    print('All the numbers are different from each other')


fun([2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 66])
fun([2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 3, 66])
