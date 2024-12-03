import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))

direction = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]
boundary = [0, 0, 0, 0]     # 동, 서, 남, 북
bottomTop = [0, 0]
curPosition = (x, y)
ans = []

while moves:
    move = moves.pop(0)
    if 0 <= curPosition[0] + direction[move][0] < n and 0 <= curPosition[1] + direction[move][1] < m:
        curPosition = (curPosition[0] + direction[move][0], curPosition[1] + direction[move][1])
        if move == 1:
            tempTop, tempBottom = boundary[1], boundary[0]
            boundary[0], boundary[1] = bottomTop[1], bottomTop[0]
        elif move == 2:
            tempTop, tempBottom = boundary[0], boundary[1]
            boundary[0], boundary[1] = bottomTop[0], bottomTop[1]
        elif move == 3:
            tempTop, tempBottom = boundary[2], boundary[3]
            boundary[2], boundary[3] = bottomTop[0], bottomTop[1]
        elif move == 4:
            tempTop, tempBottom = boundary[3], boundary[2]
            boundary[2], boundary[3] = bottomTop[1], bottomTop[0]
        bottomTop = [tempBottom, tempTop]

        if maps[curPosition[0]][curPosition[1]] != 0:
            bottomTop[0] = maps[curPosition[0]][curPosition[1]]
            maps[curPosition[0]][curPosition[1]] = 0
        else:
            maps[curPosition[0]][curPosition[1]] = bottomTop[0]
        
        ans.append(bottomTop[1])
    
print(*ans, sep = '\n')