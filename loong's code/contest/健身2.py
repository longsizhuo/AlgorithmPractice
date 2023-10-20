n, m, q = map(int, input().split())
q_time_table = set(map(int, input().split()))

training_plan = []
for _ in range(m):
    k, s = map(int, input().split())
    training_plan.append([2 ** k, s, s / (2 ** k)])

# 按单位时间收益和所需天数排序
training_plan.sort(key=lambda x: (-x[2], x[0]))

total_gain = 0

for days, gain, _ in training_plan:
    consecutive_free_days = 0
    for i in range(1, n + 1):
        if i in q_time_table:
            consecutive_free_days = 0
        else:
            consecutive_free_days += 1

        if consecutive_free_days == days:
            total_gain += gain
            for d in range(i - days + 1, i + 1):
                q_time_table.add(d)
            break

print(total_gain)
