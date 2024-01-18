from math import inf

n, needs = map(int, input().split())


class Bing:
    def __init__(self, price, storage):
        self.price = price
        self.storage = storage
        self.unitPrice = inf if storage == 0 else price / storage

    def __lt__(self, other):
        return self.price < other.price

    def __repr__(self):
        return f"bing({self.price}, {self.storage})"


storages = list(map(int, input().split()))
prices = list(map(int, input().split()))
beings = []
for i in range(n):
    beings.append(Bing(prices[i], storages[i]))
beings.sort(key=lambda x: x.unitPrice, reverse=True)
# print(beings)
shouyi = 0
for i in range(n):
    if storages[i] == 0:
        continue
    if needs >= beings[i].storage:
        needs -= beings[i].storage
        shouyi += beings[i].price
    else:
        shouyi += beings[i].unitPrice * needs
        break
print(f"{shouyi:.2f}")

