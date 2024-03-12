import sys
import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices + 1)]

    def add_edge(self, u, v, w, status):
        if status == 1:
            # 仅将活跃的公路添加到图中
            self.graph[u].append((v, w))
            self.graph[v].append((u, w))

    def min_spanning_tree_cost(self, removed_city):
        # 使用 Prim 算法计算最小生成树的成本
        visited = [False] * (self.V + 1)
        pq = [(0, 1)]  # 从城市1开始，成本为0
        total_cost = 0

        while pq:
            cost, city = heapq.heappop(pq)
            if visited[city] or city == removed_city:
                continue
            visited[city] = True
            total_cost += cost

            for neighbour, edge_cost in self.graph[city]:
                if not visited[neighbour] and neighbour != removed_city:
                    heapq.heappush(pq, (edge_cost, neighbour))

        # 检查是否所有城市都已经访问
        if all(visited[i] or i == removed_city for i in range(1, self.V + 1)):
            return total_cost
        else:
            return sys.maxsize


def find_most_critical_city(n, edges):
    g = Graph(n)
    for edge in edges:
        g.add_edge(*edge)

    max_cost = 0
    critical_cities = []
    for city in range(1, n + 1):
        cost = g.min_spanning_tree_cost(city)
        if cost > max_cost:
            max_cost = cost
            critical_cities = [city]
        elif cost == max_cost:
            critical_cities.append(city)

    return critical_cities


# 读取输入
N, M = map(int, input().split())
cities = []
for _ in range(M):
    city1, city2, cost, status = map(int, input().split())
    cities.append([city1, city2, cost, status])

# 找到最关键的城市
critical_cities = find_most_critical_city(N, cities)
print(' '.join(map(str, critical_cities)) if critical_cities else '0')
