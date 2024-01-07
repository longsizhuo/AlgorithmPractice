import math
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # 初始化最大对角线长度和最大面积
        max_diagonal = 0
        max_area = 0

        for length, width in dimensions:
            diagonal = math.sqrt(length ** 2 + width ** 2)
            area = length * width

            # 更新最大对角线长度和最大面积
            if diagonal > max_diagonal or (diagonal == max_diagonal and area > max_area):
                max_diagonal = diagonal
                max_area = area

        return max_area




print(Solution().areaOfMaxDiagonal([[9, 3], [8, 6]]))
print(Solution().areaOfMaxDiagonal([[3, 4], [4, 3]]))
print(Solution().areaOfMaxDiagonal([[1, 2], [10000000, 1]]))
