S = input()
num = len(S)
lst = []
cnt = 0
for n, m in enumerate(S):
    lst.append([n+1, m])
for a in lst:
    ori_n = a[0]
    ori_m = a[1]
    if ori_m == "A":
        for b in lst[ori_n:]:
            in_n = b[0]
            in_m = b[1]
            if in_m == "C" and (in_n - ori_n) % 2 == 0:
                if_b = lst[in_n - ((in_n - ori_n) // 2) - 1][1]
                if if_b == "B":
                    cnt += 1
print(cnt)