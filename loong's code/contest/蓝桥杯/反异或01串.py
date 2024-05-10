import os
import sys
input = sys.stdin.readline
# 请在此输入您的代码
s = input().strip()
num1 = s.count('1')
d = [0]*(2 * len(s) + 100)
r = 0
im = 0
ms = 0
ma = 0
s = '$#'+'#'.join(s)+'#^'
arr = []
for i in s:
    if i == '1':
        arr.append(1)
    else:
        arr.append(0)

for i in range(1, len(arr)):
    arr[i] += arr[i - 1]

for i in range(1,len(s)-1):
    if i <= r:
        d[i] = min(d[2*im - i],r-i)
    while(s[i - d[i] - 1] == s[ i + d[i] + 1]):
        d[i] += 1
    if i+d[i] > r:
        im,r = i, i+d[i]
    if d[i]>=ms:
        l, r = i - d[i], i + d[i]
        if arr[r] - arr[l - 1] > arr[ma + ms] - arr[ma - ms - 1]:
            ma = i
            ms = d[i]
tar = s[ma-ms:ma+ms+1].replace('#','')
# print(tar)
res = 0
n = len(tar)
if n % 2 == 0:
    res += tar.count('1') // 2
else:
    res += tar.count('1') // 2
    res += 1 if tar[n // 2] == '1' else 0

res += num1 - tar.count('1')
print(res)