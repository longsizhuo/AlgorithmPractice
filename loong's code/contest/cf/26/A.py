def strange_splitting(t, cases):
    results = []

    for case in cases:
        n, arr = case
        if len(set(arr)) == 1:  # If all elements are the same, it's impossible
            results.append("NO")
        else:
            results.append("YES")
            # We can use a simple strategy to ensure different ranges
            # We put the first element in one color and the rest in another
            result = ["R"] * n
            result[0] = "B"
            results.append("".join(result))

    return results


# Read input
t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cases.append((n, arr))

# Solve problem
results = strange_splitting(t, cases)

# Output results
for result in results:
    print(result)
