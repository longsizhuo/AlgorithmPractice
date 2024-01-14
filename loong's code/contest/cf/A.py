t = int(input())

for _ in range(t):
    n = int(input())
    unavailable = set()
    scope_down = 1
    scope_up = 1000000000

    for _ in range(n):
        a, x = map(int, input().split())
        if a == 1:
            scope_down = max(scope_down, x)
        elif a == 2:
            scope_up = min(scope_up, x)
        else:
            # 只添加在范围内的 unavailable 元素
            if scope_down <= x <= scope_up:
                unavailable.add(x)
    length = 0
    for i in unavailable:
        if scope_down <= i <= scope_up:
            length += 1

    # 如果上界小于下界，直接输出 0
    if scope_up < scope_down:
        print(0)
    else:
        print(scope_up - scope_down - length + 1)
