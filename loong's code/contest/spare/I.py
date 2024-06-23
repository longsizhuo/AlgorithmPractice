# 获取输入数据
import bisect

n, k = map(int, input().split())
temperatures = list(map(int, input().split()))
requirements = list(map(int, input().split()))

# 计算每天的冰厚度
ice_thickness = []
current_thickness = 0

for temp in temperatures:
    aaa = temp * 2
    if temp < 0:
        current_thickness += -aaa
    else:
        current_thickness = max(0, current_thickness - aaa)
    ice_thickness.append(current_thickness / 10)

results = []
ice_thickness.sort()
for i in requirements:
    index = bisect.bisect_left(ice_thickness, i)
    temp_ans = n - index
    results.append(temp_ans)

print(*results)
