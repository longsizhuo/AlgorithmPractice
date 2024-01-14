n = int(input())
s = input()

def min_swaps_to_group_boxes(n, s):
    # 将字符转换为数字方便计算
    boxes = [int(ch) for ch in s]

    # 计算红色和蓝色盒子的数量
    count_red = sum(boxes)
    count_blue = n - count_red

    # 计算蓝色盒子和红色盒子各自聚集所需的最少交换次数
    min_swaps_blue = min_swaps_for_color(boxes, 0, count_blue)
    min_swaps_red = min_swaps_for_color(boxes, 1, count_red)

    # 返回两种情况下的最小值
    return min(min_swaps_blue, min_swaps_red)

def min_swaps_for_color(boxes, color, count):
    # 计算特定颜色聚集所需的最少交换次数
    swaps_needed = 0
    color_count = 0

    # 遍历盒子，计算到达目标位置所需的交换次数
    for i, box in enumerate(boxes):
        if box == color:
            swaps_needed += i - color_count
            color_count += 1
        # 当已经统计足够数量的特定颜色盒子时停止
        if color_count == count:
            break

    return swaps_needed

# 计算最少交换次数
print(min_swaps_to_group_boxes(n, s))
