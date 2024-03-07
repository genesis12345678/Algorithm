import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())


def isPrime(num):
    for i in range(2, int(num / 2 + 1)):  # 절반까지 확인하면 된다, 에라토스테네스의 체로 최적화 가능
        if num % i == 0:
            return False
    return True


def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10):
            if i % 2 != 0:
                target = num * 10 + i
                if isPrime(target):
                    dfs(target)


dfs(2)
dfs(3)
dfs(5)
dfs(7)
