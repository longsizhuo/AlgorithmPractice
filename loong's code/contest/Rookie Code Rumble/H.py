import heapq

max_taste = 0
all_carrots = []
flag = 0
heapq.heapify(all_carrots)
for _ in range(4):
    N, A, B = map(int, input().split())
    carrots = list(map(int, input().split()))
    carrots.sort(reverse=True)
    max_taste += sum(carrots[:A])
    flag += A
    heapq.heappush(all_carrots, (-carrots[A], N, A, B - A, carrots[A:]))
K = int(input())
K -= flag
while K > 0:
    taste, N, A, B, carrots = heapq.heappop(all_carrots)
    if B > 0:
        max_taste += carrots.pop(0)
        taste = carrots[0]
        K -= 1
        B -= 1
        heapq.heappush(all_carrots, (-taste, N, A, B, carrots))
print(max_taste)
