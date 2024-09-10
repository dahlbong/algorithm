import sys

a, b, c = map(int, sys.stdin.readline().split())

def solve(a, b, c):
    if b == 1:
        return a%c
    else:
        remain = solve(a, b//2, c)
        if b%2 == 0:
            return (remain**2)%c
        else:
            return (remain**2*a)%c

print(solve(a, b, c))