from typing import List
def is_large_sum(x):
    s = str(x)
    for i in range(len(s)):
        if int(s[i]) < 1 or int(s[i]) > 18:
            return "NO"
        # 如果任何一位不能分解为两个 5-9 的数字之和，则返回 NO
        if not any(5 <= int(s[i]) - j <= 9 and 5 <= j <= 9 for j in range(10)):
            return "NO"
    return "YES"

t = int(input())
results = []
for _ in range(t):
    x = int(input())
    results.append(is_large_sum(x))

for result in results:
    print(result)