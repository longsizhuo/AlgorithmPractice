from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        xor_diff = xor_sum ^ k
        operations = 0

        # 计算需要变更的位数
        while xor_diff:
            operations += xor_diff & 1
            xor_diff >>= 1

        return operations



print(Solution().minOperations([2, 1, 3, 4], 1))
