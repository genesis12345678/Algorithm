import math

n = int(input())
A = [0] * 10_000_001

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)) + 1)):
    if A[i] != 0:
        for j in range(i * 2, len(A), i):
            A[j] = 0


def isPalindrome(target):
    temp = list(str(target))
    start = 0
    end = len(temp) - 1

    while start < end:
        if temp[start] != temp[end]:
            return False
        start += 1
        end -= 1

    return True


index = n
while True:
    if A[index] != 0 and isPalindrome(A[index]):
        print(A[index])
        break
    index += 1
