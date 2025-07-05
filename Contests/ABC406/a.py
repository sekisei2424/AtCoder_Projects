A, B, C, D = map(int, input().split())
if A > C:
    print("Yes")
else:
    if A == C and B > D:
        print("Yes")
    else:
        print("No")