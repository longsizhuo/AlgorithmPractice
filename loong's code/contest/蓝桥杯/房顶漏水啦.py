n, m = map(int, input().split())
max_x = 0  # 行的最大值
min_x = n  # 行的最小值
max_y = 0  # 列的最大值
min_y = n  # 列的最小值

for _ in range(m):
    x, y = map(int, input().split())
    max_x = max(max_x, x)
    min_x = min(min_x, x)
    max_y = max(max_y, y)
    min_y = min(min_y, y)

# 计算木板的最小边长
min_board_size = max(max_x - min_x + 1, max_y - min_y + 1)
print(min_board_size)
