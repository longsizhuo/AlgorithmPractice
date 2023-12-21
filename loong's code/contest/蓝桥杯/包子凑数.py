from functools import reduce
from math import gcd
N = int(input())
buns = []
even = 0

sum_num = 0
cheng_ji = 1
for _ in range(N):
    x = int(input())
    buns.append(x)
    if x % 2 != 0:
        even = 1
    sum_num += x
    cheng_ji *= x

if even == 0:
    print("inf")
    exit(0)


# 判断数字之间是否可以减成1
gcd_of_numbers = reduce(gcd, buns)
if gcd_of_numbers != 1:
    print("inf")
    exit(0)

# 动态规划
# Frobenius number
frobenius = cheng_ji - sum_num + 1
dp = [0 for i in range(frobenius)]
dp[0] = 1
# 有几种
for i in range(N):
    for j in range(buns[i], frobenius):
        dp[j] = max(dp[j], dp[j-buns[i]])
print(frobenius-sum(dp))
print(dp)


# 4, 5可以构成任何数。 那么2，4，7应该也可以，也就是说，只要他们可以减成1，那么就有解？

