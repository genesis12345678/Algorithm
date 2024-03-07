import sys

input = sys.stdin.readline
print = sys.stdout.write


def merge_sort(start, end):
    if start >= end:
        return

    mid = int(start + (end - start) / 2)
    merge_sort(start, mid)
    merge_sort(mid+1, end)

    for i in range(start, end + 1):
        temp[i] = a[i]

    k = start
    index1 = start
    index2 = mid + 1

    while index1 <= mid and index2 <= end:
        if temp[index1] > temp[index2]:
            a[k] = temp[index2]
            k += 1
            index2 += 1
        else:
            a[k] = temp[index1]
            k += 1
            index1 += 1

    while index1 <= mid:
        a[k] = temp[index1]
        k += 1
        index1 += 1
    while index2 <= end:
        a[k] = temp[index2]
        k += 1
        index2 += 1


n = int(input())
a = [0] * int(n+1)
temp = [0] * int(n+1)

for i in range(1,n+1):
    a[i] = int(input())

merge_sort(1, n)

result = []

for i in range(1, n+1):
    result.append(str(a[i]))

print("\n".join(result))
