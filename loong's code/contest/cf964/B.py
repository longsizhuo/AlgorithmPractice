from typing import List


def count_suneet_wins(a1, a2, b1, b2):
    matchups = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]

    win_count = 0

    for (sa1, sb1, sa2, sb2) in matchups:
        suneet_wins = (sa1 > sb1) + (sa2 > sb2)
        slavic_wins = (sa1 < sb1) + (sa2 < sb2)
        if suneet_wins > slavic_wins:
            win_count += 1

    return win_count


t = int(input())

index = 1
results = []
for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    index += 4
    result = count_suneet_wins(a1, a2, b1, b2)
    results.append(result)

for result in results:
    print(result)
