import sys
input = sys.stdin.readline

total_price = 0
N = int(input())
roads = list(map(int, input().split()))
oil = list(map(int, input().split()))
visited = [False] * (N-1)
oil.pop()
sorted_oil = sorted(oil)

while False in visited:
    oil_price = sorted_oil.pop(0)
    sum = 0

    idx = oil.index(oil_price)
    for i in range(idx, N-1):
        if visited[i] == True:
            break
        else:
            visited[i] = True
            sum += roads[i]
    total_price += sum * oil_price

print(total_price)