# C-1.16 In our implementation of the scale function (page 25), the body of the loop
# executes the command data[j] = factor. We have discussed that numeric
# types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the actual parameter sent by the caller?
def scale(data, factor):
    print(id(data[1]))
    print(id(factor))
    for j in range(len(data)):
        data[j] = factor
    print(data)
    print(factor)
    print(id(data[1]))
    print(id(factor))


s = [1, 2, 3, 4, 5, 6, 7]
scale(s, 8)

print(id(s[1]))
