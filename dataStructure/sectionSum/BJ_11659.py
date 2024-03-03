import sys

input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sumList = [0]
temp = 0
str_list = []


for i in numbers:
    temp += i
    sumList.append(temp)

for i in range(m):
    start, end = map(int, input().split())
    str_list.append(str(sumList[end] - sumList[start - 1]))

result = "\n".join(str_list)
print(result)

