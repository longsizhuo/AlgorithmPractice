# 请在此输入您的代码
n = int(input())
m = map(int, input().split())
alls = 0
for i in m:
    if i < 3:
        continue
    # 假设蓝为x，黄为x+1,红为未知y
    # 则有 y + x + x + 1 = i
    # y = i - 2x - 1
    # y要尽可能大，x要尽可能小，但是 y < x
    x = i // 3
    # (y < x < x+1)
    y = i - 2 * x - 1
    if y >= x:
        y = x - 1
    alls += y
print(alls)
