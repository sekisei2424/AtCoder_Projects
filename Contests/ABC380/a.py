N = int(input())
oc, tc, thc = 0, 0, 0
for a in str(N):
    if int(a) == 1:
        oc += 1
    elif int(a) == 2:
        tc += 1
    elif int(a) == 3:
        thc += 1
    else:
        print("No")
        break
else:
    if oc == 1 and tc == 2 and thc == 3:
        print("Yes")
    else:
        print("No")