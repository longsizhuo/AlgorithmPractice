from typing import List
def dijkstra(graph, start, end):
    import heapq
    heap = [(0, start)]
    visited = set()
    while heap:
        cost, node = heapq.heappop(heap)
        if node == end:
            return cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor))
    return -1

N, M, Q = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v, m = map(int, input().split())
    graph[u].append((v, m))
    graph[v].append((u, m))

result = []
for _ in range(Q):
    st, ed = map(int, input().split())
    result.append(dijkstra(graph, st, ed))

print('\n'.join(map(str, result)))