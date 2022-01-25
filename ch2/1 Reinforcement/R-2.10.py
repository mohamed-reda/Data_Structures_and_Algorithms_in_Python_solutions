from R_2_9 import Vector


class VectorwNeg(Vector):
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result


vv = VectorwNeg  # Use this so that I can easily change the class for subsequent exercises

v1 = vv(5)
print(v1)
# v2 = vv(5)
# for i in range(5):
#     v1[i] = 5
#     v2[i] = i
# 
# print(v1 + v2)
# print(v1 - v2)
# print(v2 - v1)
# print(-v1, v1)
