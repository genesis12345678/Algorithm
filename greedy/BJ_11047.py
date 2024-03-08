n, k = map(int, input().split())
list = [0] * n

for i in range(n):
    list[i] = int(input())

count = 0

for i in range(n - 1, -1, -1):
    if k >= list[i]:
        count += int(k / list[i])
        k = k % list[i]

print(count)