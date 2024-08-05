def func(N, M):
    seats = []
    for temp in range(N):
        seats.append(list(map(int, input().split())))
        if temp > 0:
            for i in range(M):
                if seats[temp][i] <= seats[temp - 1][i]:
                    return "No"
    else:
        return "Yes"


N, M = map(int, input().split())
print(func(N, M))
