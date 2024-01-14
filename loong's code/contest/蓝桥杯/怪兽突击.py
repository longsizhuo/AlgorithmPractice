# 接收输入
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

## 初始化动态规划数组，将所有值设置为一个很大的数
dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 0

# 动态规划填表
for i in range(1, n + 1):
    for j in range(1, k + 1):
        # 计算击败第 i 只怪兽 j 次所需的最小体力
        for x in range(j + 1):
            if i == 1:
                # 第一只怪兽特殊处理，因为可以直接挑战
                dp[i][j] = min(dp[i][j], a[0] + b[0] * x)
            else:
                # 其他怪兽需要考虑前一个怪兽的状态
                if j - x >= 0 and dp[i - 1][j - x] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - x] + a[i - 1] + b[i - 1] * x)

# 输出击败 k 次怪兽的最少体力消耗
print(min(dp[n]))