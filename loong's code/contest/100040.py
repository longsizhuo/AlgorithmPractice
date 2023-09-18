from itertools import pairwise
from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] > 0
        for i , (x, y) in enumerate(pairwise(nums)):
            if x < i+1 < y:
                ans += 1
        return ans + (nums[-1] < n)


print(Solution().countWays([1, 1]))
