t = int(input())
result = []
for _ in range(t):
    p1, p2, p3 = map(int, input().split())
    total_points = p1 + p2 + p3
    if total_points % 2 != 0 or p3 > p1 + p2:
        result.append(-1)
        continue
    total_games = (total_points + p1 + p2 + p3) // 2

    # Maximum number of draws
    max_draws = total_points // 2 - total_games

    if max_draws < 0:
        result.append(-1)
    else:
        result.append(max_draws)
print(result)
