def count_valid_pairs(A, B, S, T):
    count = 0
    for b in range(1, B + 1):
        # 计算完整周期内满足条件的a的数量
        full_cycles = A // b
        count += max(0, min(b, T + 1) - S) * full_cycles

        # 计算最后一个不完整周期
        remaining = A % b
        count += max(0, min(remaining + 1, T + 1) - S)

    return count

# 输入处理
A, B, S, T = map(int, input().split())

# 输出结果
print(count_valid_pairs(A, B, S, T))
