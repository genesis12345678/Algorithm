a, b, c = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def solution(a, b):
    temp = [0] * 2
    if b == 0:
        temp[0] = 1
        temp[1] = 0
        return temp
    quot = a // b
    v = solution(b, a % b)

    temp[0] = v[1]
    temp[1] = v[0] - v[1] * quot

    return temp


mgcd = gcd(a, b)

if c % mgcd != 0:
    print(-1)
else:
    quot = int(c / mgcd)
    temp = solution(a, b)
    print(temp[0] * quot, end=' ')
    print(temp[1] * quot)
