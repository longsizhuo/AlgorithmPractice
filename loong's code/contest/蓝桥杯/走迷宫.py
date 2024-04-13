N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
print(matrix)

x1, y1, x2, y2 = map(int, input().split())
print(x1, x2, y1, y2)
route = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]
node_x, node_y = x1, y1
depth = 0
arrived = []
while node_x != x2 or node_y != y2:
    neighbour = []
    for i, j in route:
        if 0 <= node_x + i < N and 0 <= node_y + j < M:
            if matrix[node_x + i][node_y + j] == 1:
                if [node_x + i, node_y + j] not in arrived:
                    
                neighbour.append([node_x + i, node_y + j])

