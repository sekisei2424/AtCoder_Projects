N = int(input())
T = input()
A = input()
for i, a in enumerate(T):
    if a == "o" and A[i] == "o":
        print("Yes")
        exit()
else:
    print("No")