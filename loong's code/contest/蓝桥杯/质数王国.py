def sieve_of_eratosthenes(max_num):
    """使用埃拉托斯特尼筛法生成小于等于max_num的所有质数"""
    prime = [True for _ in range(max_num + 1)]
    p = 2
    while p * p <= max_num:
        if prime[p] is True:
            for i in range(p * p, max_num + 1, p):
                prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_num) if prime[p]]
    return prime_numbers


def binary_search(primes, num):
    """在质数列表中使用二分查找来找到最接近num的质数"""
    left, right = 0, len(primes) - 1
    min_diff = float('inf')
    closest_prime = None
    while left <= right:
        mid = (left + right) // 2
        if primes[mid] == num:
            return 0
        elif primes[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

        if abs(primes[mid] - num) < min_diff:
            min_diff = abs(primes[mid] - num)
            closest_prime = primes[mid]

    return abs(closest_prime - num)


# 输入处理
n = int(input())
nums = list(map(int, input().split()))

# 预先计算质数
max_num = max(nums) * 2
primes = sieve_of_eratosthenes(max_num)

# 计算总操作次数
total_operations = sum(binary_search(primes, num) for num in nums)

# 输出结果
print(total_operations)
