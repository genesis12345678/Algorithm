import sys

input = sys.stdin.readline

n = int(input())
tree = {}  # 딕셔너리

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]  # {'root': ['left', 'child'], 'root': ['left', 'child'], ......}


def preOrder(now):
    if now == '.':
        return
    print(now, end='')
    preOrder(tree[now][0])
    preOrder(tree[now][1])


def inOrder(now):
    if now == '.':
        return
    inOrder(tree[now][0])
    print(now, end='')
    inOrder(tree[now][1])


def postOrder(now):
    if now == '.':
        return
    postOrder(tree[now][0])
    postOrder(tree[now][1])
    print(now, end='')


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
