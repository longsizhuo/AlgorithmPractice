# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 200 
#  0 <= grid[i][j] <= 200 
#  
# 
#  Related Topics 数组 动态规划 矩阵 👍 1619 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    dp[i][j] = min(grid[i][j] + dp[i - 1][j], grid[i][j] + dp[i][j - 1])
                elif i > 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
