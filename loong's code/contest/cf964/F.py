from functools import lru_cache
from statistics import median

MOD = 10 ** 9 + 7


@lru_cache(None)
def generate_combinations(n, k):
    if k == 0:
        return [[]]
    if n == 0:
        return []
    return generate_combinations(n - 1, k) + [comb + [n - 1] for comb in generate_combinations(n - 1, k - 1)]


@lru_cache(None)
def calculate_median(seq):
    seq = list(seq)
    seq.sort()
    mid = len(seq) // 2
    if len(seq) % 2 == 0:
        return (seq[mid - 1] + seq[mid]) / 2
    else:
        return seq[mid]


def find_median_sum(n, k, a):
    median_sum = 0
    combinations = generate_combinations(n, k)
    for comb in combinations:
        subseq = tuple(a[i] for i in comb)
        median = calculate_median(subseq)
        median_sum = (median_sum + median) % MOD
    return median_sum


# 输入部分
t = int(input())
test_cases = []
results = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(find_median_sum(n, k, a))
