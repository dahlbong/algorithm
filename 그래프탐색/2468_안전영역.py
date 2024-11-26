import sys
sys.setrecursionlimit(10**6)

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
result = []

rain = max(map(max, area))

def check(rain):
    safe_area = 0
    checking_area = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if area[i][j] > rain:
                checking_area[i][j] = 1
    for i in range(n):
        for j in range(n):
            if checking_area[i][j] == 1 and dfs(i, j, checking_area):
                safe_area += 1
    return safe_area

def dfs(x, y, checking_area):
    if x<0 or x>=n or y<0 or y >=n:
        return False
    if checking_area[x][y] == 1:
        checking_area[x][y] = 0
        
        dfs(x-1, y, checking_area)
        dfs(x, y-1, checking_area)
        dfs(x+1, y, checking_area)
        dfs(x, y+1, checking_area)
        return True
    return False
    
for i in range(rain):
    result.append(check(i))
    
print(max(result))
    