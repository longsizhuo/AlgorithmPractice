n = int(input())
people_distance = list(map(int, input().split()))

people_distance.sort()
sum_dis = 0
for i in range(n - 1):
    next_distance = people_distance[i + 1]
    sum_dis += max(people_distance[i], next_distance)
sum_dis += max(people_distance[-1], people_distance[0])
print(sum_dis)
