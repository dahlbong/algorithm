import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

wPower = 0
bPower = 0

def getPower(x, y, color):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque()
    sequence = 0
    q.append((x, y))

    while q:
        (x, y) = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == color and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
                sequence += 1
    if sequence == 0:
        sequence = 1

    return sequence**2

for i in range(m):
    for j in range(n):
        if visited[i][j] == True:
            continue
        elif visited[i][j] == False and graph[i][j] == 'W':
            wPower += getPower(i, j, 'W')
        elif visited[i][j] == False and graph[i][j] == 'B':
            bPower += getPower(i, j, 'B')
    
print(wPower, bPower)