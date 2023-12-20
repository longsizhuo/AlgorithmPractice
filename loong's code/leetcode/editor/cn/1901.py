class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(ii, jj):
            for i, j in direction:
                new_i, new_j = ii + i, jj + j
                # 检查新位置是否在矩阵范围内
                if 0 <= new_i < rows and 0 <= new_j < cols:
                    # 比较当前位置和其邻居的值
                    if mat[new_i][new_j] > mat[ii][jj]:
                        return dfs(new_i, new_j)
            # 如果当前位置是峰值，返回其坐标
            return [ii, jj]

        return dfs(0, 0)  # 从 (0, 0) 开始搜索

# 测试修改后的代码
print(Solution().findPeakGrid(mat=[[1, 4], [3, 2]]))
