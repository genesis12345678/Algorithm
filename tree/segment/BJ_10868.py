import sys

input = sys.stdin.readline

n, m = map(int, input().split())

treeSize = 1

while pow(2, treeSize) < n:
    treeSize += 1

leafNodeStartIndex = pow(2, treeSize)
tree = [sys.maxsize] * (pow(2, treeSize) * 2)

for i in range(leafNodeStartIndex, leafNodeStartIndex + n):
    tree[i] = int(input())


def setTree(index):
    while index > 0:
        if tree[index] < tree[index // 2]:
            tree[index // 2] = tree[index]
        index -= 1


setTree(len(tree) - 1)


def getMin(s, e):
    Min = sys.maxsize
    while s <= e:
        if s % 2 == 1:
            Min = min(Min, tree[s])
            s += 1
        if e % 2 == 0:
            Min = min(Min, tree[e])
            e -= 1

        s //= 2
        e //= 2

    return Min


result = []
for _ in range(m):
    start, end = map(int, input().split())
    start = start + leafNodeStartIndex - 1
    end = end + leafNodeStartIndex - 1
    result.append(str(getMin(start, end)))

print("\n".join(result))
