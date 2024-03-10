n = int(input())
A = [[] for _ in range(n)]
visit = [False] * n
D = [0] * n  # 각 노드 값 저장 리스트
lcm = 1  # 최소공배수


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def DFS(node):
    visit[node] = True

    for i in A[node]:
        next_node = i[0]
        if not visit[next_node]:
            D[next_node] = D[node] * i[2] // i[1]
            DFS(next_node)


for i in range(n - 1):
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

D[0] = lcm
DFS(0)
mgcd = D[0]  # 최대 공약수

for i in range(1, n):
    mgcd = gcd(mgcd, D[i])

for i in range(n):
    print(int(D[i] // mgcd), end=' ')