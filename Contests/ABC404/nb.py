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
    NL = [row[:] for row in lst]
    for i in range(N):
        for j in range(N):
            NI = j
            NJ = N - 1 - i
            NL[NI][NJ] = lst[i][j]
    return NL

print(SL)
print(right_turn(SL))