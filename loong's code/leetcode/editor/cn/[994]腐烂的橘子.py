"""
<p>在给定的&nbsp;<code>m x n</code>&nbsp;网格
 <meta charset="UTF-8" />&nbsp;<code>grid</code>&nbsp;中，每个单元格可以有以下三个值之一：</p>

<ul> 
 <li>值&nbsp;<code>0</code>&nbsp;代表空单元格；</li> 
 <li>值&nbsp;<code>1</code>&nbsp;代表新鲜橘子；</li> 
 <li>值&nbsp;<code>2</code>&nbsp;代表腐烂的橘子。</li> 
</ul>

<p>每分钟，腐烂的橘子&nbsp;<strong>周围&nbsp;4 个方向上相邻</strong> 的新鲜橘子都会腐烂。</p>

<p>返回 <em>直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回&nbsp;<code>-1</code></em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/oranges.png" style="height: 137px; width: 650px;" /></strong></p>

<pre>
<strong>输入：</strong>grid = [[2,1,1],[1,1,0],[0,1,1]]
<strong>输出：</strong>4
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[2,1,1],[0,1,1],[1,0,1]]
<strong>输出：</strong>-1
<strong>解释：</strong>左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>grid = [[0,2]]
<strong>输出：</strong>0
<strong>解释：</strong>因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>m == grid.length</code></li> 
 <li><code>n == grid[i].length</code></li> 
 <li><code>1 &lt;= m, n &lt;= 10</code></li> 
 <li><code>grid[i][j]</code> 仅为&nbsp;<code>0</code>、<code>1</code>&nbsp;或&nbsp;<code>2</code></li> 
</ul>

<div><div>Related Topics</div><div><li>广度优先搜索</li><li>数组</li><li>矩阵</li></div></div><br><div><li>👍 872</li><li>👎 0</li></div>
"""
from collections import deque
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bad_orange = deque()
        fresh_orange = 0
        # 找到所有初始腐烂的橘子
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    # 存入初始队列
                    bad_orange.append((i, j))
                elif grid[i][j] == 1:
                    fresh_orange += 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if fresh_orange == 0:
            return 0

        minutes = 0
        while bad_orange:
            minutes += 1
            for _ in range(len(bad_orange)):
                x, y = bad_orange.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) \
                            and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_orange -= 1
                        bad_orange.append((nx, ny))
        return minutes - 1 if fresh_orange == 0 else -1



# leetcode submit region end(Prohibit modification and deletion)
