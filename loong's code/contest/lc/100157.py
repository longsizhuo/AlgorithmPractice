from collections import defaultdict
from typing import List


class Solution:
    def missingInteger(self, nums):
        # 初始化顺序前缀的和
        prefix_sum = 0

        # 遍历数组
        for i in range(len(nums)):
            # 检查当前元素是否等于前一个元素加一
            if i == 0 or nums[i] == nums[i - 1] + 1:
                # 更新顺序前缀的和
                prefix_sum += nums[i]
            else:
                # 如果不满足顺序条件，则停止
                break

        # 从顺序前缀的和开始检查缺失的最小整数
        x = prefix_sum
        while x in nums:
            x += 1

        return x


# 测试
print(Solution().missingInteger(nums=[14, 9, 6, 9, 7, 9, 10, 4, 9, 9, 4, 4]))
print(Solution().missingInteger(nums=[1, 2, 3, 2, 5]))
