from collections import Counter
from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        count1, count2 = Counter(nums1), Counter(nums2)

        # 计算需要移除的元素数量
        n = len(nums1) // 2

        # 移除策略1: 优先移除在两个数组中都出现且数量大于1的元素
        for num in set(nums1) & set(nums2):
            while (count1[num] > 1 or count2[num] > 1) and n > 0 and count1[num] > 0 and count2[num] > 0:
                count1[num] -= 1
                count2[num] -= 1
                n -= 1

        # 移除策略2: 减去数量最多的元素
        if n > 0:
            for i, j in zip(count1.most_common(), count2.most_common()):
                # 同时移除两个列表中数量最多的元素
                if i[1] > n and j[1] > n:
                    count1[i[0]] -= n
                    count2[j[0]] -= n
                    return len(set(count1.elements()) | set(count2.elements()))  # 直接退出循环，因为已经移除足够的元素
                else:
                    # 如果其中一个列表的元素数量不足以全部移除，则尽可能移除，直到数量减至1或0
                    remove_count = min(i[1] - 1, j[1] - 1, n)
                    count1[i[0]] -= remove_count
                    count2[j[0]] -= remove_count
                    n -= remove_count
                    if n == 0:
                        break
        if n > 0:
            for num in set(nums1) | set(nums2):
                if count1[num] == 1 and n > 0:
                    count1[num] -= 1
                    n -= 1
                if count2[num] == 1 and n > 0:
                    count2[num] -= 1
                    n -= 1
                if n == 0:
                    break

        # print(count1, count2)
        return len(set(count1.elements()) | set(count2.elements()))


print(Solution().maximumSetSize(nums1=[1, 1, 2, 2, 3, 3], nums2=[4, 4, 5, 5, 6, 6]))
print(Solution().maximumSetSize([1, 2, 1, 2], nums2=[1, 1, 1, 1]))
print(Solution().maximumSetSize(nums1=[1, 2, 3, 4, 5, 6], nums2=[2, 3, 2, 3, 2, 3]))
print(Solution().maximumSetSize([9, 8, 4, 7], [5, 5, 9, 5]))
