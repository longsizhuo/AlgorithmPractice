from collections import Counter
from typing import List
import os
import sys

nums = int(input())
# 判断输入的字符串是否符合三带一的规则
strses = []
for i in range(nums):
    strs = input()
    if len(strs) != 4:
        strses.append("No")
        continue
    dicts = Counter(strs)
    if len(dicts) == 2:
        # print(sorted(list(dicts.values())))
        if sorted(list(dicts.values())) == [1, 3]:
            strses.append("Yes")
            continue
        else:
            strses.append("No")
            continue
    else:
        strses.append("No")
        continue
for i in strses:
    print(i)
