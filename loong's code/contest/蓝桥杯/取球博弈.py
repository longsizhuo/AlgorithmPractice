n1, n2, n3 = map(int, input().split())
x_values = list(map(int, input().split()))

max_balls = max(x_values)  # Find the maximum number of balls to process in DP
dp = ['-' for _ in range(max_balls + 1)]  # Initialize all to lose by default

# Base case: no balls left, you lose if it's your turn
dp[0] = '-'  # Cannot move, you lose

# Fill dp array
for i in range(1, max_balls + 1):
    states = []
    for n in [n1, n2, n3]:
        if i >= n:
            if dp[i - n] == '-':
                states.append('+')
            elif dp[i - n] == '+':
                states.append('-')  # Opponent wins if they were losing before
            else:
                states.append('0')  # Opponent can force a draw
    if '+' in states:
        dp[i] = '+'
    elif '0' in states and '-' not in states:
        dp[i] = '0'
    else:
        dp[i] = '-'

print(' '.join(dp[x] for x in x_values))
