from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0] * n
        # 确保 x 小于等于 y
        if x > y:
            x, y = y, x
        extra_distance = y - x

        # 直接相连的房屋对数量
        for k in range(1, n):
            # 对于距离 k，直接相连的房屋对数量
            result[k] += (n - k) * 2

        # 通过 x 和 y 的连接可能提供更短路径的情况
        for k in range(1, n):
            # x 和 y 之间，以及它们两侧的房屋对
            if k + 1 < extra_distance:
                # 当距离 k + 1 小于 x 和 y 之间的距离时，通过 x 和 y 的连接不会提供更短的路径
                continue

            # 对于 x 和 y 之间的房屋对，可以通过 x 和 y 直接连接
            if 1 <= k < extra_distance:
                result[k] += 2 * (extra_distance - k - 1)

            # 对于 x 和 y 两侧的房屋对
            # x 的左侧到 y
            if k >= extra_distance:
                left_to_y = min(x - 1, k - extra_distance + 1)
                result[k] += left_to_y * 2

            # y 的右侧到 x
            if k >= extra_distance:
                right_to_x = min(n - y, k - extra_distance + 1)
                result[k] += right_to_x * 2

        return result

# 测试代码
print(Solution().countOfPairs(5, 2, 4))
