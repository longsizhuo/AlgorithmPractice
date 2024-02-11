n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
while len(a) > 1:
    a[0] = a[0] + a[1]
    ans += a[0]
    a.pop(1)
    a.sort()

print(ans)