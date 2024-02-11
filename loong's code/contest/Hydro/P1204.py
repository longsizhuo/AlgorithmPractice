import bisect

n = int(input())
timetable = []
for _ in range(n):
    sec1, sec2 = map(int, input().split())
    i = bisect.bisect_left(timetable, [sec1])
    timetable.insert(i, [sec1, sec2])

    # 合并重叠的时间段
    merged = []
    for start, end in sorted(timetable):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    timetable = merged

# 计算最长至少有一人在挤奶的时间段
ans1 = max(end - start for start, end in timetable)

# 计算最长的无人挤奶时间段
ans2 = max((timetable[i][0] - timetable[i-1][1]) for i in range(1, len(timetable))) if len(timetable) > 1 else 0
print(ans1, ans2)
