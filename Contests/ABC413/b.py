N = int(input())
lst = []
for _ in range(N):
    S = input()
    lst.append(S)

all = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            all.append(lst[i] + lst[j])

print(len(set(all)))