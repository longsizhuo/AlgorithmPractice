print('12' < '2')
n = int(input())
cases = []
for _ in range(n):
    t = int(input())
    cases.append(t)
for t in cases:
    if t % 2 == 0:
        print('YES')
        ans = ''
        falg = 1
        while t > 0:
            if falg:
                ans += 'AA'
                t -= 2
                falg = 0
            else:
                ans += 'BB'
                t -= 2
                falg = 1
        print(ans)
    else:
        print('NO')


