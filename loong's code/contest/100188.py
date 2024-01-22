from itertools import combinations
from typing import List


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0] * n
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                # 计算最短路径
                direct = j - i
                via_xy = abs(i - x) + 1 + abs(j - y)
                via_yx = abs(i - y) + 1 + abs(j - x)
                min_distance = min(direct, via_xy, via_yx)
                # 更新结果
                result[min_distance - 1] += 1
        # 每对计数两次（i, j）和（j, i）
        return [c * 2 for c in result]


print(Solution().countOfPairs(5,2,4))