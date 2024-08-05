# C. Basil's Garden C. 罗勒花园
# http://codeforces.com/contest/1987/problem/C
t = int(input())
for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))

    seconds = 0
    while any(height > 0 for height in heights):
        new_heights = heights[:]
        for i in range(n):
            if i == n - 1 or heights[i] > heights[i + 1]:
                new_heights[i] = max(0, heights[i] - 1)
        heights = new_heights
        seconds += 1

    print(seconds)



