"""
<p>给你一个非负整数数组 <code>nums</code> 和一个整数 <code>target</code> 。</p>

<p>向数组中的每个整数前添加&nbsp;<code>'+'</code> 或 <code>'-'</code> ，然后串联起所有整数，可以构造一个 <strong>表达式</strong> ：</p>

<ul> 
 <li>例如，<code>nums = [2, 1]</code> ，可以在 <code>2</code> 之前添加 <code>'+'</code> ，在 <code>1</code> 之前添加 <code>'-'</code> ，然后串联起来得到表达式 <code>"+2-1"</code> 。</li> 
</ul>

<p>返回可以通过上述方法构造的、运算结果等于 <code>target</code> 的不同 <strong>表达式</strong> 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,1,1], target = 3
<strong>输出：</strong>5
<strong>解释：</strong>一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], target = 1
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 20</code></li> 
 <li><code>0 &lt;= nums[i] &lt;= 1000</code></li> 
 <li><code>0 &lt;= sum(nums[i]) &lt;= 1000</code></li> 
 <li><code>-1000 &lt;= target &lt;= 1000</code></li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li><li>回溯</li></div></div><br><div><li>👍 1949</li><li>👎 0</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        nums_sum = sum(nums)
        if nums_sum < target or (nums_sum - target) % 2:
            return 0
        # First sub list: P, Second: N = abs(sum(num[]))
        m, n = len(nums), (nums_sum - target) // 2
        f = [[0] * (n+1) for _ in range(m+1)]
        f[0][0] = 1
        for i, x in enumerate(nums, 1):
            for j in range(n+1):
                f[i][j] = f[i-1][j]
                if j >= x:
                    f[i][j] += f[i-1][j-x]
        return f[m][n]


# leetcode submit region end(Prohibit modification and deletion)
