from typing import List
"""
问题描述
小齐有 
�
N 个朋友，每个朋友有一个人气值 
�
�
P 
i
​
 ，小齐想最大化她能够带上电影的朋友的总人气值。每个朋友需要一定数量的 
�
�
�
�
�
�
mooney 和 
�
�
�
ice 
�
�
�
�
�
cream 
�
�
�
�
�
cones来愿意陪同小齐。每给出一定数量的 
�
�
�
ice 
�
�
�
�
�
cream 
�
�
�
�
�
cones，朋友就会提供 
1
1 个 
�
�
�
�
�
�
mooney 的折扣，但不能超过所需的 
�
�
�
�
�
�
mooney。

小齐有 
�
A 个 
�
�
�
�
�
�
mooney 和 
�
B 个 
�
�
�
ice 
�
�
�
�
�
cream 

cones。帮助她确定在最优条件下她能够达到的朋友的总人气值。

输入格式
第一行包含三个数字 N、A 和 B，表示朋友数量、mooney 数量和 ice cream cones 数量。
接下来的 N 行，每行包含三个数字 Pi 、C i  和 X i ，表示朋友的人气值、需要的 mooney 数量和提供 1 个 mooney 折扣所需的 ice cream cones 数量。

输出格式
输出小齐在最优条件下能够达到的朋友的总人气值。
"""
N, A, B = map(int, input().split())
dp = [[0] * (B + 1) for _ in range(A + 1)]

for _ in range(N):
    P, C, X = map(int, input().split())
    for a in range(A, C - 1, -1):  # 从后向前遍历mooney，仅从C开始以节约时间
        for b in range(B, -1, -1):  # 从后向前遍历ice cream cones
            # 尝试所有可能的折扣，从0到最大可能值
            for discount in range(min(b // X + 1, C + 1)):  # 限制discount不超过需要的mooney和可用的cones
                money_needed = C - discount
                if money_needed <= a:
                    dp[a][b] = max(dp[a][b], dp[a - money_needed][b - discount * X] + P)
# 输出使用最多A个mooney和B个ice cream cones所能达到的最大人气值
print(dp[A][B])



