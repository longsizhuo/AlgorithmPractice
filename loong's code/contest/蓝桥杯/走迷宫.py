from typing import List
from collections import deque


def bfs_min_steps(grid, start_x, start_y, end_x, end_y):
    n, m = len(grid), len(grid[0])
    queue = deque([(start_x - 1, start_y - 1, 0)])  # 使用0-based索引，记录步数
    visited = set()
    visited.add((start_x - 1, start_y - 1))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右，下，左，上

    while queue:
        x, y, steps = queue.popleft()

        # 如果到达终点
        if (x, y) == (end_x - 1, end_y - 1):
            return steps

        # 探索四个方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] == 1:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # 如果没有路径到达终点


# 读取输入
N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

x1, y1, x2, y2 = map(int, input().split())

# 调用BFS函数
result = bfs_min_steps(matrix, x1, y1, x2, y2)
print(result)
