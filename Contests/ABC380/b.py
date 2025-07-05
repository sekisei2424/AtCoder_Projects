S = input()
lst = []
cnt = 0
for a in S[1:]:
    if a == "|":
        lst.append(cnt)
        cnt = 0
    else:
        cnt += 1
print(*lst)