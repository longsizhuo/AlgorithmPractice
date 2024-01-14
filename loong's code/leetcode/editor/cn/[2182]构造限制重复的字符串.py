# 给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现
# 的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。 
# 
#  返回 字典序最大的 repeatLimitedString 。 
# 
#  如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 
# 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "cczazcc", repeatLimit = 3
# 输出："zzcccac"
# 解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。
# 字母 'a' 连续出现至多 1 次。
# 字母 'c' 连续出现至多 3 次。
# 字母 'z' 连续出现至多 2 次。
# 因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。
# 该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。
# 注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。
#  
# 
#  示例 2： 
# 
#  输入：s = "aababab", repeatLimit = 2
# 输出："bbabaa"
# 解释：
# 使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。 
# 字母 'a' 连续出现至多 2 次。 
# 字母 'b' 连续出现至多 2 次。 
# 因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 
# 该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。 
# 注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= repeatLimit <= s.length <= 10⁵ 
#  s 由小写英文字母组成 
#  
# 
#  Related Topics 贪心 字符串 计数 堆（优先队列） 👍 60 👎 0
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts_dict = Counter(s)
        counts = sorted(counts_dict.items(), key=lambda x: x[0], reverse=True)
        ans = ""
        released_char = []
        for i in range(len(counts)):
            if counts[i][1] < repeatLimit:
                if released_char:
                    for j in range(len(released_char)):
                        ans += counts[i][0]

                ans += counts[i][0] * repeatLimit
                del counts[i]
            else:
                release = repeatLimit - counts[i][1]
                counts[i] = (counts[i][0], release)
                ans += counts[i][0] * counts[i][1]
                # 记录还剩余的字符
                released_char.append(counts[i][0])

        return counts


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().repeatLimitedString(s="cczazcc", repeatLimit=3))
