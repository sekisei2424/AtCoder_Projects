N = int(input())
lst = []
for _  in range(N):
    A, B = map(int, input().split())
    lst.append([A, B])

cnt = 0

for m in lst:
    a, b = m[0], m[1]
    if a < b:
        cnt += 1

print(cnt)