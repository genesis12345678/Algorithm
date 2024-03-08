from queue import PriorityQueue

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    pq.put(int(input()))

total = 0
while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    sum = data1 + data2
    total += sum
    pq.put(sum)

print(total)
