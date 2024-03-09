import math

Min, Max = map(int, input().split())

check = [False] * (Max - Min + 1)

for i in range(2, int(math.sqrt(Max) + 1)):
    temp = i * i
    start_index = int(Min / temp)
    if Min % temp != 0:
        start_index += 1

    for j in range(start_index, int(Max / temp) + 1):
        check[j * temp - Min] = True

count = 0
for i in check:
    if not i:
        count += 1

print(count)
