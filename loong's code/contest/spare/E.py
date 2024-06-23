def game_winner(n, m, edges):
    def count_raids(player_positions, opponent_positions, graph):
        raids = 0
        for pos in player_positions:
            for neighbor in graph[pos]:
                if neighbor in opponent_positions:
                    raids += 1
        return raids

    def dfs(player_positions, opponent_positions, graph, turn):
        if len(player_positions) + len(opponent_positions) == n:
            return count_raids(player_positions, opponent_positions, graph)

        max_raids = -1
        for i in range(1, n + 1):
            if i not in player_positions and i not in opponent_positions:
                new_player_positions = player_positions.copy()
                new_player_positions.add(i)
                if turn == 1:
                    result = dfs(new_player_positions, opponent_positions, graph, 2)
                else:
                    result = dfs(opponent_positions, new_player_positions, graph, 1)
                max_raids = max(max_raids, result)

        return max_raids

    graph = {i: set() for i in range(1, n + 1)}
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    player_1_raids = dfs(set(), set(), graph, 1)
    player_2_raids = dfs(set(), set(), graph, 2)

    if player_1_raids > player_2_raids:
        return "player 1"
    elif player_2_raids > player_1_raids:
        return "player 2"
    else:
        return "tie"


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(game_winner(n, m, edges))
