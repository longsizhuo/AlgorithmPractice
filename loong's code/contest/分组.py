from typing import List
import os
import sys
import bisect


def can_split(heights, diff, k):
    count = 0
    i = 0
    while i < len(heights):
        count += 1
        target = heights[i] + diff
        # 使用bisect_right找到右侧边界位置
        i = bisect.bisect_right(heights, target, i)
    return count <= k


def min_difference(n, k, heights):
    heights.sort()
    low, high = 0, heights[-1] - heights[0]
    while low < high:
        mid = (low + high) // 2
        if can_split(heights, mid, k):
            high = mid
        else:
            low = mid + 1
    return low


n, k = map(int, input().split())
# n个人，k个组。
students = list(map(int, input().split()))
print(min_difference(n, k, students))
# 这个问题可以转化为一个搜索问题，我们要找到一个合适的身高差值diff，使得所有人可以分到k个组，且每个组的身高差都不超过diff。
#
# 算法的核心思路是二分搜索，对身高差进行二分搜索：
#
# 先对所有身高排序。
# 确定二分搜索的上下界。下界为0，上界为最高的身高与最矮的身高之差。
# 在上下界之间进行二分搜索，每次判断是否可以将所有人分为k个组，使得每组的身高差都不超过当前的mid。
# 如果可以分，就缩小上界为mid，否则下界为mid+1。