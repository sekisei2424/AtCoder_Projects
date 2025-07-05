N, M = map(int, input().split())
l = list(map(int, input().split()))

lst = []
for a in range(1, M+1):
    lst.append(a)

if set(lst) & set(l) != set(lst):
    print(0)
    exit()

for i in range(1, N+1):
    now_lst = l[:-i]
    for b in lst:
        if b in now_lst:
            continue
        else:
            print(i)
            exit()