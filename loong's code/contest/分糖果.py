people = list(map(int, input().split()))
leaves = people[0] % 3
people[0] = people[0] // 3
sugar = people[0]
people[-1] += people[0]

for i in range(1, len(people)):
    # 接受上个人的糖果
    people[i] += sugar
    sugar = people[i] // 3
    leaves += people[i] % 3
    people[i] = sugar
    people[i - 1] += sugar
people[0] += sugar
for i in range(len(people)):
    if i == len(people) - 1:
        print(people[i])
    else:
        print(people[i], end=' ')
print(leaves)
