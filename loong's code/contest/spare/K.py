MOD = 10 ** 9 + 7


def kudzu_kniving(a, m, queries):
    results = []
    for v in queries:
        # Determine the depth of the node v
        depth = 0
        while v >= (1 << depth):
            v -= (1 << depth)
            depth += 1

        # Number of vertices in the subtree rooted at v is 2^(a-depth)
        subtree_size = pow(2, a - depth, MOD)
        results.append(subtree_size)

    return results


# Input reading
a, m = map(int, input().split())
queries = [int(input()) for _ in range(m)]

# Get results
results = kudzu_kniving(a, m, queries)

# Output results
for result in results:
    print(result)
