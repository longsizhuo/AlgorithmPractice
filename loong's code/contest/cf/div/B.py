import heapq
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    min_args = a[0]
    needs = []
    for i in range(n):
        if a[i] < min_args:
            needs.append(min_args - a[i])
        else:
            min_args = a[i]
    ans = 0
    heapq.heapify(needs)
    already_calculated = 0
    while needs:
        min_args = heapq.heappop(needs)
        ans += (len(needs) + 2) * (min_args - already_calculated)
        already_calculated += min_args - already_calculated
    print(ans)







