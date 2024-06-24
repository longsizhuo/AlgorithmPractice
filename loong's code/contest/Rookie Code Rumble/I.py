n = int(input())


# calculate x, y
# n = x*y / x + y
def count_distinct_pairs(n):
    count = 0
    special = 0
    for x in range(n + 1, pow(n, 2) + 1):
        if (x * n) % (x - n) == 0:
            y = (x * n) // (x - n)
            if x < y:
                count += 1
            elif x == y:
                special += 1
    count = count * 2 + special
    return count


print(count_distinct_pairs(n))
