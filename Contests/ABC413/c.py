Q = int(input())
lst = []
for _ in range(Q):
    query = list(map(int, input().split()))
    lst.append(query)

A = []
rest = 0

for order in lst:
    if int(order[0]) == 1:
        for _ in range(order[1]):
            A.append(order[2])
    else:
        for _ in range(order[1]):
            rest += A.pop(0)
        print(rest)
        rest = 0
exit()