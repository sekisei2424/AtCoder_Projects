S = input()
S = ''.join(set(S))
M = "abcdefghijklmnopqrstuvwxyz"
m_lst = []
for a in M:
    m_lst.append(a)

for b in S:
    m_lst.remove(b)

print(m_lst[0])