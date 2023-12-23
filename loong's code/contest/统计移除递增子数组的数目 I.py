from typing import List


def count_removable_increasing_subarrays(nums):
    n = len(nums)
    dp = [1] * n  # 每个元素都可以单独形成一个子数组

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] += dp[j]

    return sum(dp)


# 测试示例
nums = [1, 2, 3, 4]
print(count_removable_increasing_subarrays(nums))


class Solution:
    def incremovableSubarrayCount(self, nums):
        n = len(nums)
        ans = 0

        # Function to check if the array is strictly increasing between two indices
        def is_strictly_increasing_between(start, end):
            for i in range(start, end - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        for count in range(1, n + 1):
            for left in range(n):
                right = left + count
                if right > n:
                    break

                # Check if the parts before and after the subarray are strictly increasing
                if is_strictly_increasing_between(0, left) and \
                        is_strictly_increasing_between(right, n) and \
                        (left == 0 or right == n or nums[left - 1] < nums[right]):
                    ans += 1

        return ans



nums = [8,7,6,6]
print(Solution().incremovableSubarrayCount(nums))
