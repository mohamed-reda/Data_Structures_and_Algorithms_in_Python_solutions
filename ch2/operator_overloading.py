# a1 = 10
# a2 = 20
# print(a2.__rsub__(a1))


class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a * o


a = A(10)
print(a + 30)