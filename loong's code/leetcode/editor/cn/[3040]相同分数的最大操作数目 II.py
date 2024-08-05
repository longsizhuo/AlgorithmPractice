"""
<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;，如果&nbsp;<code>nums</code>&nbsp;<strong>至少</strong>&nbsp;包含 <code>2</code>&nbsp;个元素，你可以执行以下操作中的&nbsp;<strong>任意</strong>&nbsp;一个：</p>

<ul> 
 <li>选择 <code>nums</code>&nbsp;中最前面两个元素并且删除它们。</li> 
 <li>选择 <code>nums</code>&nbsp;中最后两个元素并且删除它们。</li> 
 <li>选择 <code>nums</code>&nbsp;中第一个和最后一个元素并且删除它们。</li> 
</ul>

<p>一次操作的&nbsp;<strong>分数</strong>&nbsp;是被删除元素的和。</p>

<p>在确保<strong>&nbsp;所有操作分数相同</strong>&nbsp;的前提下，请你求出&nbsp;<strong>最多</strong>&nbsp;能进行多少次操作。</p>

<p>请你返回按照上述要求&nbsp;<strong>最多</strong>&nbsp;可以进行的操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,2,1,2,3,4]
<b>输出：</b>3
<b>解释：</b>我们执行以下操作：
- 删除前两个元素，分数为 3 + 2 = 5 ，nums = [1,2,3,4] 。
- 删除第一个元素和最后一个元素，分数为 1 + 4 = 5 ，nums = [2,3] 。
- 删除第一个元素和最后一个元素，分数为 2 + 3 = 5 ，nums = [] 。
由于 nums 为空，我们无法继续进行任何操作。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [3,2,6,1,4]
<b>输出：</b>2
<b>解释：</b>我们执行以下操作：
- 删除前两个元素，分数为 3 + 2 = 5 ，nums = [6,1,4] 。
- 删除最后两个元素，分数为 1 + 4 = 5 ，nums = [6] 。
至多进行 2 次操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>2 &lt;= nums.length &lt;= 2000</code></li> 
 <li><code>1 &lt;= nums[i] &lt;= 1000</code></li> 
</ul>

<div><div>Related Topics</div><div><li>记忆化搜索</li><li>数组</li><li>动态规划</li></div></div><br><div><li>👍 40</li><li>👎 0</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from functools import cache
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int, j:int, target:int) -> int:
            if i>= j:
                return 0
            res = 0
            if nums[i] + nums[i+1] == target:
                res = max(res, 1+dfs(i+2, j, target))
            if nums[j] + nums[j-1] == target:
                res = max(res, 1+dfs(i, j-2, target))
            if nums[i] + nums[j] == target:
                res = max(res, 1+dfs(i+1, j-1, target))
            return res

        n = len(nums)
        res1 = dfs(2, n-1, nums[0]+nums[1])
        res2 = dfs(0, n-3, nums[-2]+nums[-1])
        res3 = dfs(1, n-2, nums[0]+nums[-1])

        return max(res1, res2, res3)



# leetcode submit region end(Prohibit modification and deletion)
