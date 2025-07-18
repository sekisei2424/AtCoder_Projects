N = int(input())
A = list(map(int, input().split()))
K = int(input())

cnt = 0
for a in A:
    if K <= a:
        cnt += 1

print(cnt)