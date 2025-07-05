N = int(input())
SL, TL = [], []
for _ in range(N):
    m = input()
    l = []
    for i in m:
        l.append(i)
    SL.append(l)
for _ in range(N):
    m = input()
    l = []
    for i in m:
        l.append(i)
    TL.append(l)

def right_turn(lst):
    NL = lst
    L_cnt = 0
    for L in lst:
        cnt = 0
        for I in L:
            NL[cnt][-(L_cnt + 1)] = I
            cnt += 1
        L_cnt += 1
    return NL

print(right_turn(SL))


# def how_many_match(s, t):