def cheack(N, S):
    size = 1 << N
    dp = [False] * size     
    dp[0] = True    

    for mask in range(1, size):
        if S[mask - 1] == '1':
            continue

        for i in range(N):
            if (mask >> i) & 1:
                prev_mask = mask ^ (1 << i)

                if dp[prev_mask]:
                    dp[mask] = True
                    break   

    if dp[size - 1]:
        print("Yes")
    else:
        print("No")

T = int(input())
lst = []
for _ in range(T):
    N = int(input())
    S = input()
    cheack(N, S)