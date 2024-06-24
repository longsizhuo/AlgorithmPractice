def solve(n, last):
    for _ in range(n - 1):
        s = input()
        if s[0] != last[-1] or s in dictionary:
            return s
        last = s
        dictionary.add(s)
    else:
        return -1


n = int(input())
first = input()
dictionary = set()
dictionary.add(first)
print(solve(n, first))
