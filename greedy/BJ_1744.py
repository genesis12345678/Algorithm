from queue import PriorityQueue

n = int(input())
plusPq = PriorityQueue()
minusPq = PriorityQueue()
one = 0
zero = 0

for _ in range(n):
    num = int(input())

    if num > 1:
        plusPq.put(num * -1)
    elif num == 1:
        one += 1
    elif num == 0:
        zero += 1
    else:
        minusPq.put(num)

sum = 0

while plusPq.qsize() > 1:
    d1 = plusPq.get() * -1
    d2 = plusPq.get() * -1
    sum += d1 * d2

if plusPq.qsize() > 0:
    sum += plusPq.get() * -1

while minusPq.qsize() > 1:
    d1 = minusPq.get()
    d2 = minusPq.get()
    sum += d1 * d2

if minusPq.qsize() > 0:
    if zero == 0:
        sum += minusPq.get()

sum += one

print(sum)
