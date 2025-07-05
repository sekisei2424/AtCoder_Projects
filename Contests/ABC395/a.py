N = int(input())
A = list(map(int, input().split()))
rest = A[0]
for a in A[1:]:
    if a > rest:
        rest = a
    else:
        print("No")
        exit()
else:
    print("Yes")