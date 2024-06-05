n = int(input())
lists = list(map(int, input().split()))
lists.sort()
x = 0
for i in lists:
    x = (x * 10 + i) % 998244353
print(x)
