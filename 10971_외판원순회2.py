n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
route = []

route = []
min_cost = 4000000
visited = [False for _ in range(n)]

def dfs(city, cost):
    global min_cost
    if city == n:
        if costs[route[n-1]][route[0]] != 0:    
            min_cost = min(min_cost, cost + costs[route[n-1]][route[0]])
        return

    for i in range(n):
        if city == 0 or (not visited[i] and costs[route[city-1]][i] != 0 and min_cost > cost):
            route.append(i)
            visited[i] = True
            dfs(city + 1, cost + costs[route[city-1]][i])
            route.pop()
            visited[i] = False

dfs(0,0)
print(min_cost) 