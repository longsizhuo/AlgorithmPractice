import sys


def query(a, b):
    print(f"? {a} {b}")
    sys.stdout.flush()
    return int(input().strip())


def solve_case():
    low, high = 2, 999

    while low < high:
        mid = (low + high) // 2
        # Query a rectangle with side lengths `mid` and `mid + 1`
        result = query(mid, mid + 1)

        # If the result is (mid + 1) * (mid + 2), then x <= mid
        # Otherwise, if the result is mid * (mid + 1), then x > mid
        if result == (mid + 1) * (mid + 2):
            high = mid
        else:
            low = mid + 1

    # At this point, low should be equal to high, which is the missing x
    print(f"! {low}")
    sys.stdout.flush()


t = int(input().strip())
for _ in range(t):
    solve_case()
