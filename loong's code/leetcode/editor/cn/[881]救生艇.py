"""
<p>给定数组
 <meta charset="UTF-8" />&nbsp;<code>people</code>&nbsp;。<code>people[i]</code>表示第 <code>i</code><sup>&nbsp;</sup>个人的体重&nbsp;，<strong>船的数量不限</strong>，每艘船可以承载的最大重量为&nbsp;<code>limit</code>。</p>

<p>每艘船最多可同时载两人，但条件是这些人的重量之和最多为&nbsp;<code>limit</code>。</p>

<p>返回 <em>承载所有人所需的最小船数</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>people = [1,2], limit = 3
<strong>输出：</strong>1
<strong>解释：</strong>1 艘船载 (1, 2)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>people = [3,2,2,1], limit = 3
<strong>输出：</strong>3
<strong>解释：</strong>3 艘船分别载 (1, 2), (2) 和 (3)
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>people = [3,5,3,4], limit = 5
<strong>输出：</strong>4
<strong>解释：</strong>4 艘船分别载 (3), (3), (4), (5)</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= people.length &lt;= 5 * 10<sup>4</sup></code></li> 
 <li><code>1 &lt;= people[i] &lt;= limit &lt;= 3 * 10<sup>4</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>贪心</li><li>数组</li><li>双指针</li><li>排序</li></div></div><br><div><li>👍 331</li><li>👎 0</li></div>
"""
import bisect
import heapq
from collections import deque
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        # people = deque(people)
        while people:
            temp = limit
            temp -= people[-1]
            if temp < 0:
                continue
            index = bisect.bisect_left(people, temp)
            people.pop()
            ans += 1
            if people:
                # 说明剩下的所有都比temp小
                if index > len(people) - 1:
                    people.pop()
                elif index == 0:
                    if people[index] == temp:
                        people.pop(0)
                else:
                    people.pop(index-1)

        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().numRescueBoats(people = [1,5,3,5], limit = 7))
