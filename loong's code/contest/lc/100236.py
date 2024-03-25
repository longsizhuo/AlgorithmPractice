from typing import List


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        if c not in s:
            return 0
        return 1 if s.count(c) == 1 else s.count(c) * (s.count(c) + 1) // 2


print(Solution().countSubstrings(s="zzz", c="z"))
