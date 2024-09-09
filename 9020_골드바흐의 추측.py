import math

T = int(input())
nums = []
gold = []

for i in range(T):
    nums.append(int(input()))
    
def is_prime(x):
    x = int(x)
    if x < 2:
        return False
    
    for j in range(2, int(math.sqrt(x))+1):
        if x % j == 0:
            return False
    return True

for num in nums:
    for k in range(2, num//2 + 1):
        if is_prime(k) and is_prime(num-k):
            gold = [k, num-k]
    for g in gold:
        print(g, end=" ")
    print('')
