N, M = map(int, input().split())
s_lst, t_lst = [], []
for _ in range(N):
    l = []
    con = input()
    for a in con:
        l.append(a)
    s_lst.append(l)
for _ in range(M):
    l = []
    con = input()
    for a in con:
        l.append(a)
    t_lst.append(l)

if N == M:
    print(1, 1)

dif = N - M + 1
for r in range(dif):
    rest_lst, r_rest_lst = [], []
    for m in s_lst:
        rest_lst.append(m[r:r+M])
    for n in range(dif):
        r_rest_lst = rest_lst[n:n+M]
        if r_rest_lst == t_lst:
            print(n+1, r+1)
            exit()