n = int(input())
mountains = list(map(int, input().split()))


def count_peaks(n, heights):
    if n == 1:
        return 1

    peaks = 0
    i = 0

    while i < n:
        # Find the start of a plateau
        start = i
        while i < n - 1 and heights[i] == heights[i + 1]:
            i += 1

        # i is now the end of the plateau
        end = i

        # Check if the current point is a peak
        if (start == 0 or heights[start] > heights[start - 1]) and (end == n - 1 or heights[end] > heights[end + 1]):
            peaks += 1

        i += 1

    return peaks


print(count_peaks(n, mountains))
