from collections import deque

A = deque(input())
B = deque(input())
length = min(len(A), len(B))
i, j = 0, 0
slices = []

desk = []
def function(A, B, desk, slices):
    while len(A) != 0 and len(B) != 0:
        desk.append(A.popleft())
        if A[0] in desk:
            temp = A[0]
            slic = desk[desk.index(temp):]
            if slic in slices:
                return -1
            slices.append(slic)
            A.extend(slic)
            desk = desk[:desk.index(temp)]
            A, B = B, A
        desk.append(B.popleft())
        if B[0] in desk:
            temp = B[0]
            slic = desk[desk.index(temp):]
            if slic in slices:
                return -1
            slices.append(slic)
            B.extend(slic)
            desk = desk[:desk.index(temp)]
            A, B = B, A
        # A.popleft()
        # B.popleft()

        print("desk:", desk)
        print("A:", A,"\nB:", B)
    return A if B is None else B
print("".join(list(function(A,B,desk,slices))))
