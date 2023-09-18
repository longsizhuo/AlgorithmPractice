from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # 下标转化成二进制
        index = [bin(i)[2:] for i in range(len(nums))]
        # 统计每个数中1的个数，如果==k，将其十进制数计入列表

        ans = []
        for i in range(len(nums)):
            if index[i].count('1') == k:
                ans.append(nums[i])      # print(nums)
        # print(nums)
        return sum(ans)

print(Solution().sumIndicesWithKSetBits([5, 10, 1, 5,2], 1))