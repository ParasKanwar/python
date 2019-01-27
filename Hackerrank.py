
# this was a problem from www.hackerrank.com (Name = left rotation)

import math
import os
import random
import re
import sys
from collections import deque


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = deque(
        map(int, input("enter the list of numbers : ").rstrip().split()))

queue = deque(a)


def leftRotation(list1, count, rotations):
    temp = deque([])
    for i in range(rotations):
        tem = list1.popleft()
        temp.append(tem)

    return list1+temp


answer = leftRotation(a, n, d)

print(*answer)
# print(leftRotation(a, n))
