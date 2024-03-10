t = int(input())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


ans = []

for _ in range(t):
    a, b = map(int, input().split())
    result = a * b // gcd(a, b)
    ans.append(str(result))

print("\n".join(ans))