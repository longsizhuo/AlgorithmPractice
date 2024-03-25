from typing import List
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(0, len(s)-1):
            if s[i:i+2][::-1] in s:
                return True
        return False

print(Solution().isSubstringPresent("abcd"))