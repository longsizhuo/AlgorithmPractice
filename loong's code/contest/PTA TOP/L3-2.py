# 水果忍者
n = int(input())
# n条直线的坐标
lines = []
y_values = set()
min_x = float('inf')
max_x = float('-inf')

for _ in range(n):
    x, y1, y2 = map(int, input().split())
    lines.append([x, y1, y2])
    y_values.update([y1, y2])
    min_x = min(min_x, x)
    max_x = max(max_x, x)

# 对y值排序
y_values = sorted(y_values)

# 遍历y坐标
for i in range(len(y_values)):
    for j in range(i, len(y_values)):
        y1, y2 = y_values[i], y_values[j]
        if y1 == y2:
            continue

        # 计算直线的斜率
        slope = (y2 - y1) / (max_x - min_x)

        # 检查直线是否与所有x坐标上的竖线相交
        flag = True
        for x, line_y1, line_y2 in lines:
            y_at_x = y1 + slope * (x - min_x)
            if not (min(line_y1, line_y2) <= y_at_x <= max(line_y1, line_y2)):
                flag = False
                break

        if flag:
            print(min_x, y1, max_x, y2)
            exit()
