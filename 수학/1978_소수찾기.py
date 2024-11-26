import math

N = int(input())
nums = input().split(' ')
prime = 0

def is_prime(x):
    x = int(x)
    if x == 1:
        return False
    
    for j in range(2, int(math.sqrt(x))+1):
        if x % j == 0 and x != 2:
            return False
    return True

for i in range(N):
    if is_prime(nums[i]):
        prime += 1

print(prime)