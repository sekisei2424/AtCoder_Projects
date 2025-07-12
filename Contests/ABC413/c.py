import collections

Q = int(input())
lst = []
for _ in range(Q):
    lst.append(list(map(int, input().split())))

A = collections.deque()

for order in lst:
    Q_type = order[0]

    if Q_type == 1:
        cnt = order[1]
        value = order[2]
        A.append((value, cnt))
    else:
        rm_cnt = order[1]
        rest = 0

        while rm_cnt > 0 and A:
            f_value, f_cnt = A.popleft()

            if rm_cnt >= f_cnt:
                rest += f_value * f_cnt
                rm_cnt -= f_cnt
            else:
                rest += f_value * rm_cnt
                A.appendleft((f_value, f_cnt - rm_cnt))
                rm_cnt = 0
        
        print(rest)