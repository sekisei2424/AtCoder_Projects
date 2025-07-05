""" 

def judge(lst):
    if not lst[0] < lst[1]:
        return False
    if not judge_big(lst):
        return False
    if not judge_small(lst):
        return False
    return True
    

def judge_big(lst):
    cnt = 0
    for i in range(1, len(lst) - 1):
        if lst[i-1] < lst[i] > lst[i+1]:
            cnt += 1
        if cnt > 1:
            return False
    return cnt == 1

def judge_small(lst):
    cnt = 0
    for i in range(1, len(lst) - 1):
        if lst[i-1] > lst[i] < lst[i+1]:
            cnt += 1
        if cnt > 1:
            return False
    return cnt == 1

print(judge(P)) """

N = int(input())
P = list(map(int, input().split()))

cnt = 0

for i in range(N):
    big_cnt = 0
    small_cnt = 0
    
    if i + 2 >= N:
        continue

    if P[i] >= P[i+1]:
        continue

    for j in range(i+3, N+1):
        now_lst = P[i:j]
        if now_lst[0] >= now_lst[1]:
            continue

        big_cnt = 0
        small_cnt = 0
        for a in range(1, len(now_lst) - 1):
            if now_lst[a - 1] < now_lst[a] > now_lst[a + 1]:
                big_cnt += 1
            elif now_lst[a - 1] > now_lst[a] < now_lst[a + 1]:
                small_cnt += 1
            
            if big_cnt > 1 or small_cnt > 1:
                break
        
        if big_cnt == 1 and small_cnt == 1:
            cnt += 1
    
print(cnt)