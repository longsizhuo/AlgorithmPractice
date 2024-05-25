# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
#
#
#
#  示例 1:
#
#
#
#
# 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# 输出: 4
# 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
#
#
#  示例 2:
#
#
#
#
# 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# 输出: 10
#
#
#
#
#  提示:
#
#
#  m == heightMap.length
#  n == heightMap[i].length
#  1 <= m, n <= 200
#  0 <= heightMap[i][j] <= 2 * 10⁴
#
#
#
#
#  Related Topics 广度优先搜索 数组 矩阵 堆（优先队列） 👍 728 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or len(heightMap) == 0:
            return 0
        n, m = len(heightMap), len(heightMap[0])
        visited = [[False] * m for _ in range(n)]
        hq = []
        heapq.heapify(hq)
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    heapq.heappush(hq, (heightMap[i][j], i, j))
                    visited[i][j] = True
        res = 0
        dirs = [-1, 0, 1, 0, -1]
        while hq:
            height, x, y = heapq.heappop(hq)
            for k in range(4):
                nx = x + dirs[k]
                ny = y + dirs[k + 1]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if height > heightMap[nx][ny]:
                        res += height - heightMap[nx][ny]
                    heapq.heappush(hq, (max(heightMap[nx][ny], height), nx, ny))
                    visited[nx][ny] = True
        return res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().trapRainWater(
    heightMap=[[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))
