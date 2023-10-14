# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。 
# 
#  你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1 ： 
# 
#  
# 输入：nums = [2,2,1]
# 输出：1
#  
# 
#  示例 2 ： 
# 
#  
# 输入：nums = [4,1,2,1,2]
# 输出：4
#  
# 
#  示例 3 ： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -3 * 10⁴ <= nums[i] <= 3 * 10⁴ 
#  除了某个元素只出现一次以外，其余每个元素均出现两次。 
#  
# 
#  Related Topics 位运算 数组 👍 3000 👎 0
from typing import List
from collections import Counter

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 位运算
        # 0 ^ x = x
        # x ^ x = 0
        # a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
        # a ^ b ^ c ^ a ^ b = (a ^ a) ^ (b ^ b) ^ c = 0 ^ 0 ^ c = c
        s = Counter(nums)
        for k, v in s.items():
            if v == 1:
                return k
        return -1
# leetcode submit region end(Prohibit modification and deletion)
