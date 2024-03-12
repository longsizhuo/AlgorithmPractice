from typing import List
import bisect
n, q = map(int, input().split())
intervals = [list(map(int, input().split())) for _ in range(n)]
intervals.sort(key=lambda x: x[0])
for _ in range(q):
    a, b = map(int, input().split())
    count = 0
    # 二分查找, 寻找包含a但是不包含b的区间
    left = bisect.bisect_left(intervals, [a, 0])
    right = bisect.bisect_right(intervals, [b, 0])
    for i in range(left, right):
        if intervals[i][1] > b:
            count += 1
    print(count)

