N, M = map(int, input().split())
d_lst = [0] * (N + 1)
lst = [0] * N

for _ in range(M):
    L, R = map(int, input().split())
    d_lst[L] += 1
    if R < N:
        d_lst[R + 1] -= 1

lst[0] = d_lst[1]

for i, j in enumerate(d_lst[2:]):
    lst[i + 1] = lst[i] + j

print(min(lst))