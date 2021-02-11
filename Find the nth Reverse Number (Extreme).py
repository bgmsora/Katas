import math

def find_reverse_number(n):
    if n == 1: return 0
    n -= 1
    m = n/18
    p = max(-1,math.floor(math.log10(m)))
    if m <= (pow(10,p+1)-1)/9:
        k = 2*(p+1)
        n -= 11*pow(10,p) - 2
    elif m <= (pow(10,p+1)-1)/9 + pow(10,p+1)/2:
        k = 2*(p+1) + 1
        n -= 2*(pow(10,p+1)-1)
    else:
        k = 2*(p+1) + 2
        n -= 11*pow(10,p+1) - 2
    q = (k+1)//2
    x = n - 1 + pow(10,(k-1)//2)
    y = x * pow(10,k//2)
    if k % 2 == 1: x //= 10
    i = k//2 - 1
    while i >= 0:
        y += (x%10) * pow(10,i)
        i -= 1
        x //= 10
    return y