S = input()
T = input()

judge_lst = []
rest = S[0]

for m in S[1:]:
    if m.isupper():
        judge_lst.append(rest)
    rest = m

t_lst = []
for l in T:
    t_lst.append(l)

if set(judge_lst).issubset(t_lst):
    print("Yes")
else:
    print("No")