from typing import List
t = int(input())
for _ in range(t):
    n = int(input())
    cakes = list(map(int, input().split()))

    # Alice starts first
    alice_eaten = 0
    alice_max_tastiness = -1

    # Sort the cakes in descending order to always let Alice pick the biggest available suitable cake
    cakes.sort(reverse=True)

    for i in range(n):
        if i % 2 == 0:
            # Alice's turn
            for j in range(n):
                if cakes[j] > alice_max_tastiness:
                    alice_max_tastiness = cakes[j]
                    cakes[j] = -1  # Mark this cake as eaten by Alice
                    alice_eaten += 1
                    break
        else:
            # Bob's turn
            for j in range(n):
                if cakes[j] != -1:
                    cakes[j] = -1  # Mark this cake as eaten by Bob
                    break

    print(alice_eaten)
