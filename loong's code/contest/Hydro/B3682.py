n, k = map(int, input().split())
dicts = {}
storage = set()
dicts_2 = {
    "1": 2000,
    "2": 1000,
    "3": 200,
    "4": 36,
    "5": 6,
}
ans = 0
for _ in range(n):
    quality, code = input().split()
    dicts[quality] = code
for _ in range(k):
    bonus = input()
    if bonus not in storage:
        storage.add(bonus)
    else:
        ans += dicts_2[dicts[bonus]]
print(ans)



