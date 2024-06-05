# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。 
# 
#  异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, p.length <= 3 * 10⁴ 
#  s 和 p 仅包含小写字母 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 1446 👎 0
from collections import Counter, deque
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_dict = Counter(p)
        stack_dict = Counter(s[:len(p)])
        stack = deque(s[:len(p)])
        # 初始化ans
        if stack_dict == p_dict:
            ans = [0]
        else:
            ans = []
        # 构建初始栈
        for ind in range(len(p), len(s)):
            temp_char = stack.popleft()
            stack_dict[temp_char] -= 1
            stack.append(s[ind])
            stack_dict[s[ind]] += 1
            if stack_dict == p_dict:
                ans.append(ind - len(p) + 1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().findAnagrams(s="abab", p="ab"))
