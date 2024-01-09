# 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中
#  i 和 j 之间的距离和 i 和 k 之间的欧式距离相等（需要考虑元组的顺序）。 
# 
#  返回平面上所有回旋镖的数量。 
# 
#  示例 1： 
# 
#  
# 输入：points = [[0,0],[1,0],[2,0]]
# 输出：2
# 解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
#  
# 
#  示例 2： 
# 
#  
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：points = [[1,1]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == points.length 
#  1 <= n <= 500 
#  points[i].length == 2 
#  -10⁴ <= xi, yi <= 10⁴ 
#  所有点都 互不相同 
#  
# 
#  Related Topics 数组 哈希表 数学 👍 286 👎 0
from collections import Counter
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
import math
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0

        points.sort()
        for x1, y1 in points:
            cnt = Counter()
            for x2, y2 in points:
                d2 = (x1-x2)**2+(y1-y2)**2
                ans += cnt[d2]*2
                cnt[d2] += 1
        return ans









# leetcode submit region end(Prohibit modification and deletion)
print(Solution().numberOfBoomerangs(points=[[0,0],[1,0],[0,2]]))