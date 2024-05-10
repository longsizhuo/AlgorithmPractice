N = list(map(int, input().split()))
N = sorted(N)
for i in N:
    print(i, end=" ")
N=N[::-1]
print()
for i in N:
    print(i, end=" ")
