# L3-1 天梯地图
import heapq

n, m = map(int, input().split())
# 读取地图
maps = []


def dijkstra(graph, start, optimize):
    # 'optimize' is a string that decides if we optimize for 'time' or 'distance'
    n = len(graph)
    visited = [False] * n
    dist = [float('inf')] * n
    dist[start] = 0
    path = [-1] * n

    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True

        for neighbor, length, time in graph[node]:
            if optimize == 'time':
                cost = time
            else:  # optimize for 'distance'
                cost = length

            if dist[node] + cost < dist[neighbor]:
                dist[neighbor] = dist[node] + cost
                path[neighbor] = node
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist, path


graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2, one_way, length, time = map(int, input().split())
    graph[v1].append((v2, length, time))
    if not one_way:
        graph[v2].append((v1, length, time))

start, end = map(int, input().split())

dist_time, path_time = dijkstra(graph, start, 'time')


def print_path(path, end):
    route = []
    while end != -1:
        route.append(end)
        end = path[end]
    return ' => '.join(map(str, route[::-1]))


dist_distance, path_distance = dijkstra(graph, start, 'distance')
if path_time[end] == path_distance[end]:
    print(f"Time = {dist_time[end]}; Distance = {dist_distance[end]}: {print_path(path_time, end)}")
else:
    print(f"Time = {dist_time[end]}: {print_path(path_time, end)}")
    print(f"Distance = {dist_distance[end]}: {print_path(path_distance, end)}")
