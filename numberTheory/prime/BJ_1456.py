import math

min, max = map(int, input().split())
A = [0] * 10_000_001

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)) + 1)):
    if A[i] != 0:
        for j in range(i * 2, len(A), i):
            A[j] = 0

count = 0

for i in range(2, 10_000_001):
    if A[i] != 0:
        temp = A[i]
        while A[i] <= max / temp:
            if A[i] >= min / temp:
                count += 1
            temp *= A[i]

print(count)