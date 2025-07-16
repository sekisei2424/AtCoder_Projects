N = int(input())
S = input()
T = input()

cnt = 0

for n, a in enumerate(S):
    if a != T[n]:
        cnt += 1

print(cnt)