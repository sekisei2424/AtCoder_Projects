N = int(input())
A = list(map(int, input().split()))

def sigma(nums):
    s = sum(nums)
    sq_s = sum(x * x for x in A)
    return (s * s - sq_s) // 2

print(sigma(A))