"""
<p>一个下标从 <strong>0</strong>&nbsp;开始的数组的 <strong>交替和</strong>&nbsp;定义为 <strong>偶数</strong>&nbsp;下标处元素之 <strong>和</strong>&nbsp;减去 <strong>奇数</strong>&nbsp;下标处元素之 <strong>和</strong>&nbsp;。</p>

<ul> 
 <li>比方说，数组&nbsp;<code>[4,2,5,3]</code>&nbsp;的交替和为&nbsp;<code>(4 + 5) - (2 + 3) = 4</code>&nbsp;。</li> 
</ul>

<p>给你一个数组&nbsp;<code>nums</code>&nbsp;，请你返回&nbsp;<code>nums</code>&nbsp;中任意子序列的&nbsp;<strong>最大交替和</strong>&nbsp;（子序列的下标 <strong>重新</strong>&nbsp;从 0 开始编号）。</p>

<ul> 
</ul>

<p>一个数组的 <strong>子序列</strong>&nbsp;是从原数组中删除一些元素后（也可能一个也不删除）剩余元素不改变顺序组成的数组。比方说，<code>[2,7,4]</code>&nbsp;是&nbsp;<code>[4,<strong>2</strong>,3,<strong>7</strong>,2,1,<strong>4</strong>]</code>&nbsp;的一个子序列（加粗元素），但是&nbsp;<code>[2,4,2]</code> 不是。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre><b>输入：</b>nums = [<strong>4</strong>,<strong>2</strong>,<strong>5</strong>,3]
<b>输出：</b>7
<b>解释：</b>最优子序列为 [4,2,5] ，交替和为 (4 + 5) - 2 = 7 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [5,6,7,<strong>8</strong>]
<b>输出：</b>8
<b>解释：</b>最优子序列为 [8] ，交替和为 8 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [<strong>6</strong>,2,<strong>1</strong>,2,4,<strong>5</strong>]
<b>输出：</b>10
<b>解释：</b>最优子序列为 [6,1,5] ，交替和为 (6 + 5) - 1 = 10 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li> 
 <li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li></div></div><br><div><li>👍 129</li><li>👎 0</li></div>
"""
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n+1)
        g = [0] * (n+1)
        for ind, x in enumerate(nums, 1):
            f[ind] = max(g[ind-1]-x, f[ind-1])
            g[ind] = max(f[ind-1]+x, g[ind-1])
        return max(f[n],g[n])



# leetcode submit region end(Prohibit modification and deletion)
