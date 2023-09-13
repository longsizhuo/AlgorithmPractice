# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。 
# 
#  数值（按顺序）可以分成以下几个部分： 
# 
#  
#  若干空格 
#  一个 小数 或者 整数 
#  （可选）一个 'e' 或 'E' ，后面跟着一个 整数 
#  若干空格 
#  
# 
#  小数（按顺序）可以分成以下几个部分： 
# 
#  
#  （可选）一个符号字符（'+' 或 '-'） 
#  下述格式之一： 
#  
#  至少一位数字，后面跟着一个点 '.' 
#  至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字 
#  一个点 '.' ，后面跟着至少一位数字 
#  
#  
# 
#  整数（按顺序）可以分成以下几个部分： 
# 
#  
#  （可选）一个符号字符（'+' 或 '-'） 
#  至少一位数字 
#  
# 
#  部分数值列举如下： 
# 
#  
#  ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"] 
#  
# 
#  部分非数值列举如下： 
# 
#  
#  ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"] 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "0"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "e"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "."
# 输出：false 
# 
#  示例 4： 
# 
#  
# 输入：s = "    .1  "
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 20 
#  s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。 
#  
# 
#  Related Topics 字符串 👍 548 👎 0
import re


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isNumber(self, s: str) -> bool:
        n, l, r = len(s), 0, len(s) - 1
        while l < n and s[l] == ' ':
            l += 1
        while r >= 0 and s[r] == ' ':
            r -= 1
        if l > r:
            return False
        s = s[l:r + 1].replace('e', 'E')
        n, idx = len(s), 0
        while idx < n and s[idx] != 'E':
            idx += 1
        if idx == n:
            return self.check(s, True)
        else:
            return self.check(s[:idx], True) and self.check(s[idx + 1:], False)

    def check(self, s: str, is_decimal: bool) -> bool:
        if s == "." or s == "":
            return False
        n, cnt = len(s), 0
        for i in range(n):
            c = s[i]
            if c == '+' or c == '-':
                if i != 0 or i == n - 1:
                    return False
            elif c == '.':
                if not is_decimal:
                    return False
                if cnt != 0:
                    return False
                a = i - 1 >= 0 and s[i - 1].isdigit()
                b = i + 1 < n and s[i + 1].isdigit()
                if not (a or b):
                    return False
                cnt += 1
            elif not c.isdigit():
                return False
        return True



# leetcode submit region end(Prohibit modification and deletion)

print(Solution().isNumber("46.e3"))


def test_isNumber():
    s = Solution()
    tests = ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123", "12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
    for test in tests:
        print(f"Testing '{test}': {s.isNumber(test)}")


test_isNumber()
