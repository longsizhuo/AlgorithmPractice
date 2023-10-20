n = int(input().strip())
S = input().strip()
T = input().strip()

swapped = T.swapcase() * 2
index = swapped.find(S)
if index != -1:
    print("Yes")
    print(min(index, n - index))
else:
    print("No")


# jupyter 的分割
# %% [python]
def rabin_karp_search(text, pattern, d, q):
    # d is the number of characters in the input alphabet
    # q is a prime number used as mod

    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    p = 0
    t = 0

    # preprocessing: calculate hash values for pattern and text's first window
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:  # if hash values match, then check character by character
            if pattern == text[s:s + m]:
                return s
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q

    return -1


def main():
    n = int(input().strip())
    S = input().strip()
    T = input().strip()

    swapped = T.swapcase() * 2

    index = rabin_karp_search(swapped, S, 256, 1000000007)

    if index != -1:
        print("Yes")
        print(min(index, n - index))
    else:
        print("No")


main()
