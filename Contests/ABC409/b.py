N = int(input())
A = list(map(int, input().split()))
index = 0
AS = sorted(A, reverse=True)

for i, a in enumerate(AS):
    if a >= i + 1:
        index = i + 1
    else:
        break

print(index)