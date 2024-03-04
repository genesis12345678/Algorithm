import sys
from collections import deque


class Node:

    def __init__(self, index, value):
        self.index = index
        self.value = value


input = sys.stdin.readline

n, l = map(int, input().split())

myDeque = deque()
now = list(map(int, input().split()))

result_list = []

for i in range(n):
    while myDeque and myDeque[-1].value > now[i]:
        myDeque.pop()

    myDeque.append(Node(i, now[i]))

    if myDeque[0].index <= i - l:
        myDeque.popleft()

    result_list.append(str(myDeque[0].value))

print(" ".join(result_list))
