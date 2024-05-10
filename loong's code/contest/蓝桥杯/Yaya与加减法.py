from collections import deque

n, A, B = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a)
ans = 0

while a:
    if a[0] < 0 and B > 0:  # 有负数且还有减号可用
        ans -= a.popleft()  # 将负数转为正数加到总和中
        B -= 1
    elif A > 0:  # 使用加号处理剩余的数
        ans += a.pop()  # 正数直接加到总和中
        A -= 1
    else:
        break  # 没有操作符可用时停止

print(ans)
