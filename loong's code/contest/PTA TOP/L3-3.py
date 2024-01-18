from itertools import combinations

string = list(input())
#  至多删三个字符, 有多少种不同的结果
ans = set()
n = len(string)
for i in range(0, 3 + 1):
    for indices in combinations(string, n-1):
        substring = ''.join([string[i] for i in range(n) if i not in indices])
        ans.add(substring)
print(len(ans))
