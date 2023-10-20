# 一共n天，m个训练计划，q个其他安排
n, m, q = map(int, input().split())

# 被占用的日期
q_time_table = set(map(int, input().split()))

training_plan = []
for _ in range(m):
    # 需要2**k天，收益为s
    k, s = map(int, input().split())
    training_plan.append([2 ** k, s, s / (2 ** k)])

training_plan.sort(key=lambda x: x[0])

# 动态规划
dp = [0] * (n + 1)

# dp[i] 表示第i天的最大收益, 如果第i天被占用，则dp[i] = dp[i-1]
for i in range(1, n + 1):
    dp[i] = dp[i-1]
    for days, gain, _ in training_plan:
        if i - days + 1 < 1:
            continue
        if not any(day in q_time_table for day in range(i - days + 1, i + 1)):
            dp[i] = max(dp[i], dp[i - days] + gain)

print(dp[n])
