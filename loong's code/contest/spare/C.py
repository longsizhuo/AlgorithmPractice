import heapq
from collections import defaultdict


def solve():
    n, m = map(int, input().split())
    s, t, c = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(m):
        u, v, p = map(int, input().split())
        edges[u].append((v, p))
        edges[v].append((u, p))

    # distance array initialized to negative infinity
    dist = [-float('inf')] * (n + 1)
    dist[s] = c
    # max heap to store the number of candies and the country
    queue = [(-c, s)]

    while queue:
        candies, u = heapq.heappop(queue)
        candies = -candies

        if u == t:
            return candies

        if candies < dist[u]:
            continue

        for v, p in edges[u]:
            # Calculate the number of candies left after paying the tax
            next_candies = candies * (100 - p) // 100
            if next_candies > dist[v]:
                dist[v] = next_candies
                heapq.heappush(queue, (-next_candies, v))

    return dist[t]


print(solve())
