import bisect

n = int(input())
trains = list(map(int, input().split()))
rails = []

for train in trains:
    pos = bisect.bisect_left(rails, train, key=lambda x: x[-1])
    if pos == len(rails):
        rails.append([train])
    else:
        rails[pos].append(train)

print(len(rails))
