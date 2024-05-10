n, k = map(int, input().split())
chocolate = [list(map(int, input().split())) for _ in range(n)]
front, tail = 1, 100000


def find(edge_len):
    global k
    ans = 0
    for wid, hei in chocolate:
        ans += (wid // edge_len) * (hei // edge_len)
        if ans >= k:
            return True
    return False


while front <= tail:
    mid = (front + tail) // 2
    if not find(mid):
        tail = mid - 1
    else:
        front = mid + 1
print(tail)
