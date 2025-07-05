N, K = map(int, input().split())
A = list(map(int, input().split()))

def math(n1, n2):
    n = n1 * n2
    if check(n):
        return n
    else:
        return 1
    
def check(result):
    ans = str(result)
    return (len(ans) <= K)

rest = A[0]
cnt = 2

for i in A[1:]:
    rest = math(rest, i)

print(rest)