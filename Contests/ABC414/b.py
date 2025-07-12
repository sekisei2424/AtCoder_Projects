flag = False
N = int(input())
lst = []
for _ in range(N):
    c, l = map(str, input().split())
    if int(l) > 100:
        flag = True
    lst.append([c, l])

if flag == True:
    print("Too Long")
    exit()

m = ""

for a in lst:
    m += a[0] * int(a[1])
    if len(m) > 100:
        print("Too Long")
        exit()

print(m)