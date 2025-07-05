N, M = map(int, input().split())
lst = []
for i in range(M):
    lst.append(i)

A = list(map(int, input().split()))

for n in range(M):
    for a in set(A[:-(n+1)]):
        print("A now:", A[:-(n+1)])
        if a in lst:
            break
    else:
        print(M)
        exit()