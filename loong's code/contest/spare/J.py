from functools import cache


def find_mole_spies(n, weights):
    @cache
    def can_partition(arr):
        total = sum(arr)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in arr:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]

    total_weight = sum(weights)
    possible_moles = []

    for i in range(n):
        if can_partition(weights[:i] + weights[i + 1:]):
            possible_moles.append(i + 1)

    return possible_moles


# 读取输入
n = int(input().strip())
weights = list(map(int, input().strip().split()))

# 解决问题
possible_moles = find_mole_spies(n, weights)

# 输出结果
print(len(possible_moles))
print(" ".join(map(str, possible_moles)))
