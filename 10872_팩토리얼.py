# import sys
# sys.getrecursionlimit(10**6)

def fac(i):
    if i>0:
        return i * fac(i-1)
    else:
        return 1
    
# n = int(input())
# print(fac(n))

import math

n = int(input())
print(math.factorial(n))
