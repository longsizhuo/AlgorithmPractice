# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。 
# 
#  由于答案可能很大，因此 返回答案模 10^9 + 7 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。 
# 
#  示例 2： 
# 
#  
# 输入：arr = [11,81,94,43,3]
# 输出：444
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 3 * 10⁴ 
#  1 <= arr[i] <= 3 * 10⁴ 
#  
# 
#  
# 
#  Related Topics 栈 数组 动态规划 单调栈 👍 761 👎 0
from typing import List
from itertools import combinations


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stk = []
        for i, v in enumerate(arr):
            while stk and arr[stk[-1]] >= v:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        stk = []
        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        mod = 10**9 + 7
        return sum((i - left[i]) * (right[i] - i) * v for i, v in enumerate(arr)) % mod



# leetcode submit region end(Prohibit modification and deletion)
print(Solution().sumSubarrayMins(arr=[3, 1, 2, 4]))
