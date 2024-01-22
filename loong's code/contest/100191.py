class Solution:
    def minimumPushes(self, word: str) -> int:
        # 映射2-9的8个栈
        ditcs = {}
        n = len(word)
        ans = 0
        flag = 1
        while n > 0:
            if n < 8:
                ans += (n*flag)
                n = 0
                break
            else:
                ans += (8*flag)
                n -= 8
            flag += 1
        return ans

print(Solution().minimumPushes("xyzxyzxyzxyz"))


