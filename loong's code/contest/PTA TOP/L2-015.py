from collections import deque

n, k, m = map(int, input().split())

grades = deque()
for i in range(n):
    nums = list(map(int, input().split()))
    grade = (sum(nums) - max(nums) - min(nums)) / (k - 2)
    grades.append(grade)

grades = sorted(grades)
output = ' '.join(f"{grade:.3f}" for grade in grades[-m:])
print(output)
