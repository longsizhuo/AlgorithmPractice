from functools import cache
from itertools import combinations

string = input()
#  至多删三个字符, 有多少种不同的结果
result = set()
n = len(string)


def dfs(s, index, removed, current, results):
    if removed > 3:
        return  # 如果删除的字符超过三个，停止搜索
    if index == len(s):
        results.add(current)  # 添加到结果集中
        return
    # 不删除当前字符的情况
    dfs(s, index + 1, removed, current + s[index], results)
    # 删除当前字符的情况
    dfs(s, index + 1, removed + 1, current, results)


dfs(string, 0, 0, '', result)
print(len(result))
