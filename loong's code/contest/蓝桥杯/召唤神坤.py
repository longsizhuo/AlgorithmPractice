# n = int(input())
# w = list(map(int, input().split()))
# ans = -1
# # i 的取值范围: [0 - len(w)-2]
# # j 的取值范围: [i+1 - len(w)-1]
# # k 的取值范围: [j+1 - len(w)]
# for i in range(len(w) - 2):
#     for j in range(i + 1, len(w) - 1):
#         for k in range(j + 1, len(w)):
#             ans = max(ans, (w[i] + w[k]) // w[j])
# print(ans)

def maxDanceValue(w):
    n = len(w)
    max_value = 0

    # 预处理前缀最小值
    min_wi = [float('inf')] * n
    min_wi[0] = w[0]
    for i in range(1, n):
        min_wi[i] = min(min_wi[i-1], w[i])

    # 预处理后缀最小值
    min_wk = [float('inf')] * n
    min_wk[n-1] = w[n-1]
    for k in range(n-2, -1, -1):
        min_wk[k] = min(min_wk[k+1], w[k])

    for j in range(1, n-1):
        if min_wi[j-1] + min_wk[j+1] < float('inf'):
            max_value = max(max_value, w[j] // (min_wi[j-1] + min_wk[j+1]))
    return

n = int(input())
w = list(map(int, input().split()))
def max_dance_value_corrected(N, W):
    # 初始化最大团队舞力值为0
    max_value = 0

    # 从左向右遍历，记录每个位置左侧的最大舞力值
    max_left = [0] * N
    max_val = 0
    for i in range(N):
        max_val = max(max_val, W[i])
        max_left[i] = max_val

    # 从右向左遍历，记录每个位置右侧的最大舞力值
    max_right = [0] * N
    max_val = 0
    for i in range(N-1, -1, -1):
        max_val = max(max_val, W[i])
        max_right[i] = max_val

    # 计算每个 j 的最大舞力值
    for j in range(1, N - 1):
        max_value = max(max_value, (max_left[j-1] + max_right[j+1]) // W[j])

    return max_value

print(max_dance_value_corrected(n, w))
