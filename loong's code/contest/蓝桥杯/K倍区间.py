# from functools import cache
#
# N, K = map(int, input().split())
# num_list = []
# for _ in range(N):
#     num_list.append(int(input()))
#
# # 前缀和
# prefix_sum_mod = 0
# count = 0
# mod_count = {0: 1}
# ans = []
#
# for i in num_list:
#     prefix_sum_mod = (prefix_sum_mod + i) % K
#     count += mod_count.get(prefix_sum_mod, 0)
#     ans.append(prefix_sum_mod)
#     mod_count[prefix_sum_mod] = mod_count.get(prefix_sum_mod, 0) + 1
#
# print(count)
# print(ans)


def findKMultipleSubarrays(N, K, arr):
    prefix_sum_mod = 0
    mod_positions = {0: [-1]}  # 初始化为-1，代表从数组开始到当前位置
    subarrays = []

    for i, num in enumerate(arr):
        prefix_sum_mod = (prefix_sum_mod + num) % K
        if prefix_sum_mod in mod_positions:
            for start in mod_positions[prefix_sum_mod]:
                subarrays.append(arr[start + 1: i + 1])
        mod_positions.setdefault(prefix_sum_mod, []).append(i)

    return subarrays


# # 找到所有符合条件的子数组
# subarrays = findKMultipleSubarrays(N, K, num_list)
# for subarray in subarrays:
#     print(subarray)


def countKMultipleSubarrays(arr, K):
    # 初始化前缀和模数为0的次数
    mod_count = {0: 1}
    # 初始化前缀和和K倍区间的数量
    prefix_sum = 0
    count = 0

    # 遍历数组，计算前缀和并进行模K运算
    for num in arr:
        # 计算当前的前缀和
        prefix_sum += num
        # 计算前缀和对K取模的结果
        mod = prefix_sum % K
        # 如果此前已经出现过相同的模数，则找到了一个K倍区间
        count += mod_count.get(mod, 0)
        # 更新该模数出现的次数
        mod_count[mod] = mod_count.get(mod, 0) + 1

    return count


# 测试代码
arr = [1, 2, 3, 4, 5]
K = 2
print(countKMultipleSubarrays(arr, K) ) # 应该返回6
