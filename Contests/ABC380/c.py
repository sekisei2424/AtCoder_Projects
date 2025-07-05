N, K = map(int, input().split())
S = input()
unity_cnt = 0
cnt = 0
one, two, three, four = "", "", "", ""
status = 0
now = ""
for a in S:
    if a == "1":
        if status == 0:
            if unity_cnt == K - 1:
                two = now
                status = 1
                now = a
            else:
                status = 1
                now += a
        else:
            now += a
    else:
        if status == 1:
            status = 0
            unity_cnt += 1
            if unity_cnt == K - 1:
                one = now
                now = a
            elif unity_cnt == K:
                three = now
                now = a
            else:
                now += a
        else:
            now += a
four = now
if three == "":
    print(one + four + two)
else:
    print(one + three + two + four)
""" print(one)
print(two)
print(three)
print(four) """