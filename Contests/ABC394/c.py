S = input()
def to_AC(s):
    judge = False
    r = ""
    cnt = 0
    w_cnt = 0
    for a in s:
        r += a
        if a == "W":
            if judge == True:
                w_cnt += 1
            else:
                judge = True
        elif a == "A" and judge == True:
                r = r[:-1 * (2 + w_cnt)]
                r += "AC"
                r += "C" * w_cnt
                cnt += 1
                w_cnt = 0
                judge = False
        else:
            judge = False
    if cnt == 0:
        return False
    else:
        return r
    
for _ in range(len(S)):
    if to_AC(S) == False:
        break
    else:
        S = to_AC(S)
print(S)