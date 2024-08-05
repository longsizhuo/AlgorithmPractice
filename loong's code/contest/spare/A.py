x, y = map(int, input().split())
r = int(input())
min_x = x - r
max_x = x + r
min_y = y - r
max_y = y + r
print(min_x, max_y)
print(max_x, max_y)
print(max_x, min_y)
print(min_x, min_y)
