N, M, C = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]

prefixSum = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        prefixSum[i][j] = nums[i-1][j-1] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]

maxValue = -1000000000
bestX, bestY = 0, 0

for i in range(1, N-C+2):
    for j in range(1, M-C+2):
        valueSum = prefixSum[i+C-1][j+C-1] - prefixSum[i-1][j+C-1] - prefixSum[i+C-1][j-1] + prefixSum[i-1][j-1]
        if valueSum > maxValue:
            maxValue = valueSum
            bestX, bestY = i, j

print(bestX, bestY)
