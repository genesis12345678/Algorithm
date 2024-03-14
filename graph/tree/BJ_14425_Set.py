import sys

input = sys.stdin.readline

n, m = map(int, input().split())
text = set([input() for _ in range(n)])

count = 0

for _ in range(m):
    data = input()
    if data in text:
        count += 1

print(count)