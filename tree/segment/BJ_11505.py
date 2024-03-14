import sys

input = sys.stdin.readline
print = sys.stdout.write
n, m, k = map(int, input().split())
MOD = 1_000_000_007

exp = 1
while pow(2, exp) < n:
    exp += 1

treeSize = pow(2, exp) * 2
leafNodeStartIndex = pow(2, exp)
tree = [1] * treeSize

for i in range(leafNodeStartIndex, leafNodeStartIndex + n):
    tree[i] = int(input())


def setTree(index):
    while index > 0:
        tree[index // 2] *= tree[index] % MOD
        index -= 1


setTree(treeSize - 1)


def changeValue(index, value):
    tree[index] = value
    while index > 0:
        index //= 2
        tree[index] = (tree[index * 2] * tree[index * 2 + 1]) % MOD


def getMultiple(s, e):
    temp = 1
    while s <= e:
        if s % 2 == 1:
            temp = temp * tree[s] % MOD
            s += 1
        if e % 2 == 0:
            temp = temp * tree[e] % MOD
            e -= 1

        s //= 2
        e //= 2

    return temp


result = []

for _ in range(m + k):
    q, s, e = map(int, input().split())

    if q == 1:
        s = s + leafNodeStartIndex - 1
        changeValue(s, e)
    else:
        s = s + leafNodeStartIndex - 1
        e = e + leafNodeStartIndex - 1
        result.append(str(getMultiple(s, e)))

print("\n".join(result))
