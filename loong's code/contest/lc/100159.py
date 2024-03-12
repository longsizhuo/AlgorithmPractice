from collections import deque
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        # 使用队列来进行广度优先搜索
        queue = deque([(x, 0)])  # (当前值, 操作次数)
        visited = set()  # 用于记录已经访问过的值，避免重复处理

        while queue:
            current, steps = queue.popleft()
            if current == y:
                return steps
            visited.add(current)

            # 对四种操作进行探索
            if current % 11 == 0 and current // 11 not in visited:
                queue.append((current // 11, steps + 1))
            if current % 5 == 0 and current // 5 not in visited:
                queue.append((current // 5, steps + 1))
            if current - 1 not in visited:
                queue.append((current - 1, steps + 1))
            if current + 1 not in visited:
                queue.append((current + 1, steps + 1))

        return -1  # 如果无法使 x 和 y 相等，则返回 -1



print(Solution().minimumOperationsToMakeEqual(26,1))