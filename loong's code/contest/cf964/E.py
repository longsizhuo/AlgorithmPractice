def min_operations_to_zero(n):
    operations = 0
    while n > 0:
        n = n // 3
        operations += 1
    return operations

t = int(input())
results = []
for _ in range(t):
    l, r = map(int, input().split())
    total_operations = 0
    oper = min_operations_to_zero(l)
    for n in range(l+1, r+1):
        total_operations += min_operations_to_zero(n)
        # print(n, total_operations)
    total_operations += oper*2

    results.append(total_operations)

for result in results:
    print(result)
