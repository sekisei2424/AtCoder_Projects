N, M = map(int, input().split())
A = list(map(int, input().split()))
s = 0
for a in A:
    s += a
if s <= M:
    print("Yes")
else:
    print("No")