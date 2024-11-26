import sys
input = sys.stdin.readline

n, k, dish, coupon = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
for i in range(dish-1):
    sushi.append(sushi[i])
ans = [[0, 1] for _ in range(n)]

temp = []
same = []
for i in range(dish):
    if sushi[i] in temp:
        same.append(sushi[i])
    if sushi[i] == coupon:
        ans[0][1] = 0
    temp.append(sushi[i])
ans[0][0] = len(temp) - len(same)

for i in range(dish, n+dish-1):
    cur = temp.pop(0)
    next = sushi[i]

    if cur != next:
        if cur == coupon and cur not in same:
            ans[i-dish+1][1] = 1
        elif next == coupon:
            ans[i-dish+1][1] = 0
        else:
            ans[i-dish+1][1] = ans[i-dish][1]

        if next in temp:
            ans[i-dish+1][0] = ans[i-dish][0]
            same.append(next)
        else:
            ans[i-dish+1][0] = ans[i-dish][0] + 1

        if cur in same:
            same.pop(same.index(cur))
        else:
            ans[i-dish+1][0] -= 1

    else:      
        ans[i-dish+1][0] = ans[i-dish][0]
        ans[i-dish+1][1] = ans[i-dish][1]
    temp.append(next)
    
ans.sort(key=lambda x: (-x[0], -x[1]))
print(sum(ans[0]))