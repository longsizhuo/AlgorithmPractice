def dfs(x, y, maps, visited):
    if (x, y) in visited:  # 如果当前位置已经被访问过，则结束当前尝试
        return False
    if x == 1 and y == len(maps[0]) - 1:  # 如果到达(2,n)（考虑索引从0开始）
        return True

    visited.add((x, y))  # 将当前位置加入已访问集

    # 机器人的四个可能的自主移动方向
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        # 确保新位置在网格内
        if 0 <= new_x < 2 and 0 <= new_y < len(maps[0]):
            # 模拟箭头指示的移动
            if maps[new_x][new_y] == '<':
                arrow_x, arrow_y = new_x, new_y - 1
            else:  # maps[new_x][new_y] == '>'
                arrow_x, arrow_y = new_x, new_y + 1
            if 0 <= new_x < 2 and 0 <= new_y < len(maps[0]):
                # 如果新位置未被访问过，继续探索
                if (arrow_x, arrow_y) not in visited:
                    if dfs(arrow_x, arrow_y, maps, set(visited)):  # 注意我们传递一个已访问位置的拷贝
                        return True

    return False  # 如果没有其他路径可以尝试，返回False


t = int(input())
Maps = []
for _ in range(t):
    maps = []
    n = int(input())
    for _ in range(2):
        maps.append(list(input()))
    Maps.append(maps)
for maps in Maps:
    ans = 'NO'
    # 机器人从左上角开始
    if dfs(0, 0, maps, set()):
        ans = 'YES'
    print(ans)
