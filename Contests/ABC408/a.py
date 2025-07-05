N, S = map(int, input().split())
T = list(map(int, input().split()))
rest = 0
for a in T:
    if a - rest > S:
        print("No")
        exit()
    rest = a
else:
    print("Yes")