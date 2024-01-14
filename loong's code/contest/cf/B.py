t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    # Bob的策略：将最大的x个正数乘以-1
    a.sort(reverse=True)
    for i in range(min(x, n)):
        if a[i] > 0:
            a[i] *= -1
    a.sort(reverse=True)
    print(a)

    for i in range(len(a) - 1, -1, -1):
        if k == 0:
            break
        if a[i] < 0:
            a.pop()
            k -= 1
        else:
            break
    print(sum(a))
