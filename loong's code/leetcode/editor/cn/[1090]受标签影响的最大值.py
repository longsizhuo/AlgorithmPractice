"""
<p>我们有一个&nbsp;<code>n</code>&nbsp;项的集合。给出两个整数数组&nbsp;<code>values</code>&nbsp;和 <code>labels</code>&nbsp;，第 <code>i</code> 个元素的值和标签分别是&nbsp;<code>values[i]</code>&nbsp;和&nbsp;<code>labels[i]</code>。还会给出两个整数&nbsp;<code>numWanted</code>&nbsp;和 <code>useLimit</code> 。</p>

<p>从 <code>n</code> 个元素中选择一个子集 <code>s</code> :</p>

<ul> 
 <li>子集 <code>s</code> 的大小&nbsp;<strong>小于或等于</strong> <code>numWanted</code> 。</li> 
 <li><code>s</code> 中 <strong>最多</strong> 有相同标签的 <code>useLimit</code> 项。</li> 
</ul>

<p>一个子集的&nbsp;<strong>分数&nbsp;</strong>是该子集的值之和。</p>

<p>返回子集&nbsp;<code>s</code> 的最大 <strong>分数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
<strong>输出：</strong>9
<strong>解释：</strong>选出的子集是第一项，第三项和第五项。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
<strong>输出：</strong>12
<strong>解释：</strong>选出的子集是第一项，第二项和第三项。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
<strong>输出：</strong>16
<strong>解释：</strong>选出的子集是第一项和第四项。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>n == values.length == labels.length</code></li> 
 <li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li> 
 <li><code>0 &lt;= values[i], labels[i] &lt;= 2 * 10<sup>4</sup></code></li> 
 <li><code>1 &lt;= numWanted, useLimit &lt;= n</code></li> 
</ul>

<div><div>Related Topics</div><div><li>贪心</li><li>数组</li><li>哈希表</li><li>计数</li><li>排序</li></div></div><br><div><li>👍 80</li><li>👎 0</li></div>
"""
import operator
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        """

        :rtype: int
        """
        dictionary = zip(values, labels)
        # 这个地方不要用dict，否则会忽略掉相同的key
        used = {}
        ans = 0
        dictionary = sorted(dictionary, reverse=True)
        for j, i in dictionary:
            if i in used:
                if used[i] < useLimit:
                    used[i] += 1
                    ans += j
            else:
                used[i] = 1
                ans += j
            if sum(used.values()) == numWanted:
                break
        print(dictionary, "\n", used)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
