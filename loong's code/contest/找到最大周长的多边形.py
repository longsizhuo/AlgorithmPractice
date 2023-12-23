from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        left = 0
        sums = sum(nums)
        for ind, i in enumerate(nums):
            sums -= i
            if sums > i:
                return sums + i
            else:
                continue
        return -1


print(Solution().largestPerimeter([1,12,1,2,5,50,3]))