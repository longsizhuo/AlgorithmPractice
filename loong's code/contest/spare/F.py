from collections import deque


def fridge_distraction(n, t):
    # Generate the items in alphabetical order
    items = deque([chr(i) for i in range(ord('a'), ord('a') + n)])

    # Store the result items
    result = []
    while t > 0:
        if t >= n:
            # If t is greater than or equal to n, then we can add all items
            char = items.pop()
            result.append(char)
            items.appendleft(char)
            t -= n
        else:
            result.append(items[t - 1])
            break
    # Output the number of items and the sequence
    print(len(result))
    print(' '.join(result))


n, t = map(int, input().split())
fridge_distraction(n, t)
