import collections

Q = int(input())
lst = []
for _ in range(Q):
    query = list(map(int, input().split()))
    lst.append(query)

A = collections.deque()
rest = 0

for order in lst:
    if int(order[0]) == 1:
        for _ in range(order[1]):
            A.append(order[2])
    else:
        for _ in range(order[1]):
            if A:
                rest += A.popleft()
            else:
                break
        print(rest)
        rest = 0