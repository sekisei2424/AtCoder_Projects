N, L, R = map(int, input().split())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])

cnt = 0
for a in lst:
    X, Y = a[0], a[1]
    if X <= L and R <= Y:
        cnt += 1
print(cnt)