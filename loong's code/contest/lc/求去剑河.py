n = int(input())
nums = list(map(int, input().split()))
m = int(input())
# 计算前缀和
sums = [0] * (n + 1)
for i in range(1, n + 1):
    sums[i] = sums[i - 1] + nums[i - 1]
# 计算区间和
for i in range(m):
    l, r = map(int, input().split())
    print(sums[r] - sums[l - 1])

