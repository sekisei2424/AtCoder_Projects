A = int(input())
N = int(input())

# 10進法 → n進法

def tenToN(n10, nA):
    str_n = ""
    while n10:
        if n10 % nA >= 10:
            return -1
        str_n += str(n10 % nA)
        n10 //= nA
    return str_n[::-1]

ans = 0

k = 1

while True:
    s = str(k)

    odd_s = s + s[:-1][::-1]
    odd = int(odd_s)

    if odd > N:
        break

    toA_odd = tenToN(odd, A)
    if toA_odd != -1 and toA_odd == toA_odd[::-1]:
        ans += odd
    
    even_s = s + s[::-1]
    even = int(even_s)

    if even > N:
        k += 1
        continue

    toA_even = tenToN(even, A)
    if toA_even != -1 and toA_even == toA_even[::-1]:
        ans += even
    
    k += 1

print(ans)