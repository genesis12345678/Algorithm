n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
target_list = list(map(int, input().split()))

for i in range(m):
    find = False
    target = target_list[i]

    start = 0
    end = n - 1

    while start <= end:
        midIdx = int((start + end) / 2)
        midVal = A[midIdx]

        if midVal > target:
            end = midIdx - 1
        elif midVal < target:
            start = midIdx + 1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)