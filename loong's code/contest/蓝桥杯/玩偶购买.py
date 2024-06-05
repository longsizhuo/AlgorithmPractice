t = int(input())
results = []
for _ in range(t):
    lists = list(map(int, input().split()))
    n, x, y, a, b = lists
    dp = [[[0] * (b + 1) for _ in range(a + 1)] for _ in range(n + 1)]
    max_dolls = 0

    for i in range(1, n + 1):
        for j in range(a, -1, -1):
            for k in range(b, -1, -1):
                if j >= x:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - x][k] + 1)
                if k >= y:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - y] + 1)
                max_dolls = max(max_dolls, dp[i][j][k])

    results.append(max_dolls if max_dolls > 0 else -1)
print(results)
