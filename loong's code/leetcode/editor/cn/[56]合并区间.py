# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 10⁴ 
#  
# 
#  Related Topics 数组 排序 👍 2333 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先按区间的起始位置进行排序
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果merged列表为空，或者当前区间不与merged列表中的最后一个区间重叠，直接添加到merged列表
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则我们就合并当前区间和merged列表中的最后一个区间
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    # leetcode submit region end(Prohibit modification and deletion)


print(Solution().merge(intervals=[[1, 4], [2, 3], [8, 10], [15, 18]]))
