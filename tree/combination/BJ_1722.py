factorial = [0] * 21
permut = [0] * 21
visit = [False] * 21
n = int(input())

factorial[0] = 1
for i in range(1, n + 1):
    factorial[i] = factorial[i - 1] * i

data = list(map(int, input().split()))

if data[0] == 1:
    k = data[1]
    for i in range(1, n + 1):
        cnt = 1
        for j in range(1, n + 1):
            if not visit[j]:            # N자리의 순열을 정할 때는 N-1번째 순열의 경우의 수를 이용한다.
                # 주어진 k에 따라 각 자리에 들어갈 수 있는 수 찾기
                if k <= cnt * factorial[n - i]:     # 주어진 값(k)과 현재 자리 - 1에서 만들 수 있는 경우의 수 비교
                    k -= factorial[n - i] * (cnt - 1)   # k가 더 작아지면 k를 k = k - 경우의 수 * (cnt - 1)로 업데이트한다.
                    permut[i] = j       # k가 더 작아지면 순열에 값을 저장한다.
                    visit[j] = True
                    break
                cnt += 1

    for i in range(1, n + 1):
        print(permut[i], end=' ')

else:
    k = 1
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, data[i]):
            if not visit[j]:        # 현재 자릿수의 숫자를 확인하고 해당 숫자보다 앞 숫자 중 미사용 숫자를 카운트
                cnt += 1
        k += cnt * factorial[n - i]     # 미사용 숫자 * (현재 자리 - 1에서 만들 수 있는 순열의 개수) 를 k에 더한다.
        visit[data[i]] = True

    print(k)
