
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

last = n
left, right = 0, n - 1
mood = sum(a)
# 前缀和
wood_qianzuihe = [0] * (n + 1)
for i in range(1, n + 1):
    wood_qianzuihe[i] = wood_qianzuihe[i - 1] + a[i - 1]


# 剩下的木材数：
def caculate_last_wood(index):
    return wood_qianzuihe[n] - wood_qianzuihe[index] - a[index] * (n - index)


def half_search(left, right, m):
    res = -1
    while left <= right:
        mid = (left + right) // 2
        # 计算当前高度砍伐的木材量
        wood = caculate_last_wood(mid)
        # 如果砍伐的木材量大于等于m
        if wood >= m:
            res = mid  # 记录当前满足条件的索引
            left = mid + 1  # 尝试找一个更高的砍伐点
        else:
            right = mid - 1  # 否则降低砍伐点

    # 如果没有找到合适的高度，返回-1
    if res == -1:
        return -1

    # 确定砍伐高度在哪两个树木之间
    # 从res索引对应的树的高度开始，向下逐一减小高度，直到木材量小于m
    cut_height = a[res]
    while cut_height > 0 and caculate_last_wood(res) + (a[res] - cut_height) * (n - res) >= m:
        cut_height -= 1

    return cut_height + 1


ind = half_search(left, right,m)
print(ind)
print(a[ind])
