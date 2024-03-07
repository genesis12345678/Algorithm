import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
count = [0] * 10001

for i in range(n):
    count[int(input())] += 1

result = []

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(str(i) + "\n")
