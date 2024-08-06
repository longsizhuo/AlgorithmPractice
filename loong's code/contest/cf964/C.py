import sys
from typing import List


def function(times, n: int, s: int, m: int):
    # 按照开始时间排序
    times.sort(key=lambda x: x[0])
    # 检查时间间隔是否大于s
    if times[0][0] >= s:
        print("YES")
        return
    for i in range(1, n):
        if times[i][0] - times[i - 1][1] >= s:
            print("YES")
            return
    if m - times[-1][1] >= s:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    n, s, m = map(int, input().split())
    times = []
    for _ in range(n):
        time_begin, time_end = map(int, input().split())
        times.append((time_begin, time_end))
    function(times, n, s, m)
