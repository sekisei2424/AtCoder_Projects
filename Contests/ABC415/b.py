S = input()
lst = []
for n, a in enumerate(S):
    if a == "#":
        lst.append(n + 1)
    if len(lst) == 2:
        print(str(lst[0]) + "," + str(lst[1]))
        lst = []