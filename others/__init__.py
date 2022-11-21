# d = {}
# print(type(d))
# for t in range(int(input())):
#     n = int(input())
#     l = list(map(int, input().split()))
#     d = {}
#     #
#     for i in l:
#         d[i] = d.get(i, 0) + 1
#         if d[i] >= 3:
#             print(i)
#             break
#     else:
#         print(-1)

#         # dict

# print(9 + 11 + 11 + 11 + 10 + 10 + 11)
# x = 0
# x = (x * 15 + 3) % 7
# print(x)
# x = (x * 15 + 3) % 7
# print(x)
# x = (x * 15 + 3) % 7
# print(x)
# x = (x * 15 + 3) % 7
# print(x)
# x = (x * 15 + 3) % 7
# print(x)
# x = (x * 15 + 3) % 7
# print(x)
# x = (x * 15 + 3) % 7
# print(x)
from typing import Optional


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()


def isPalindrome(head: SLinkedList):
    # bol = False
    # print(head.headval)
    # for i in range(int(len(head.headval) / 2)):
    #     if head[i] == head[-i - 1]:
    #         bol = True
    #     else:
    #         bol = False
    #         break

    arr = []
    while head:
        arr.append(head.val)
        head = head.last
    if arr == arr[::-1]:
        return True
    else:
        return False
