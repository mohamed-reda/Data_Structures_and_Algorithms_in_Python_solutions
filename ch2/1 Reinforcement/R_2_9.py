class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

# v1 = Vector(5)
# 
# v2 = Vector(5)
# for i in range(5):
#     v1[i] = 5
#     v2[i] = i
# print(v1)
# print(v1 + v2)
# print(v1 - v2)
# print(v2 - v1)
