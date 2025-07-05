N, L = map(int, input().split())
d = list(map(int, input().split()))
TN, lst, now, ans = L // 3, [0] * L, 0, 0

if L % 3 != 0:
    print(0)
    exit()

lst[0] += 1
for a in d:
    now = (now + a) % L
    lst[now] += 1

for b in range(TN):
    ans += lst[b] * lst[b + TN] * lst[b + TN + TN]

print(ans)