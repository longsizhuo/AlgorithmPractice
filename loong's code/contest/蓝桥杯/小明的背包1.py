from typing import List
N, V = map(int, input().split())
items = []
for _ in range(N):
    items.append(list(map(int, input().split())))
dp = [0] * (V + 1)
for i in range(N):
    w, v = items[i]
    for j in range(V, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
print(dp[V])