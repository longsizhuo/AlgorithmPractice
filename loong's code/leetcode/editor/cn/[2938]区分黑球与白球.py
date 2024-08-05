"""
<p>桌子上有 <code>n</code> 个球，每个球的颜色不是黑色，就是白色。</p>

<p>给你一个长度为 <code>n</code> 、下标从 <strong>0</strong> 开始的二进制字符串 <code>s</code>，其中 <code>1</code> 和 <code>0</code> 分别代表黑色和白色的球。</p>

<p>在每一步中，你可以选择两个相邻的球并交换它们。</p>

<p>返回「将所有黑色球都移到右侧，所有白色球都移到左侧所需的 <strong>最小步数</strong>」。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "101"
<strong>输出：</strong>1
<strong>解释：</strong>我们可以按以下方式将所有黑色球移到右侧：
- 交换 s[0] 和 s[1]，s = "011"。
最开始，1 没有都在右侧，需要至少 1 步将其移到右侧。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "100"
<strong>输出：</strong>2
<strong>解释：</strong>我们可以按以下方式将所有黑色球移到右侧：
- 交换 s[0] 和 s[1]，s = "010"。
- 交换 s[1] 和 s[2]，s = "001"。
可以证明所需的最小步数为 2 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "0111"
<strong>输出：</strong>0
<strong>解释：</strong>所有黑色球都已经在右侧。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li> 
 <li><code>s[i]</code> 不是 <code>'0'</code>，就是 <code>'1'</code>。</li> 
</ul>

<div><div>Related Topics</div><div><li>贪心</li><li>双指针</li><li>字符串</li></div></div><br><div><li>👍 39</li><li>👎 0</li></div>
"""
from collections import deque


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSteps(self, s: str) -> int:
        left, right = 0, len(s) - 1
        cnt = 0

        while left < right:
            while left < right and s[left] == '0':
                left += 1
            while left < right and s[right] == '1':
                right -= 1

            if left < right:
                cnt += 1
                left += 1
                right -= 1

        return cnt




# leetcode submit region end(Prohibit modification and deletion)
print(Solution().minimumSteps(s="101"))