def print_histogram(data):
    max_height = max(data.values())  # 找到最高的柱子高度
    keys = sorted(data.keys())  # 获取所有的键并排序

    # 逐行打印直方图
    for i in range(max_height, 0, -1):
        line = ''
        for key in keys:
            if data[key] >= i:
                line += '#'
            else:
                line += '.'
        print(line)

    # 打印底部的横线
    print('-' * n)


n, s, k = map(int, input().split())

lists = list(map(int, input().split()))

histogram = {}

for i in range(n):
    histogram[i] = 0

for i in lists:
    temp = i - 1
    histogram[temp // s] += 1
print_histogram(histogram)
