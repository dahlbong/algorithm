import sys
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]        # 북, 동, 남, 서
cnt = 0

def clean(x, y, dir):
    room[x][y] = 2
    # 동서남북 중 청소할 곳 O
    for i in range(dir+3, dir-1, -1):     
        nd = i % 4
        nx, ny = x + directions[nd][0], y + directions[nd][1]
        if room[nx][ny] == 0:
            return clean(nx, ny, nd)
    
    # 동서남북 중 청소할 곳 X
    bd = (dir + 2) % 4
    bx, by = x + directions[bd][0], y + directions[bd][1]
    if room[bx][by] != 1:
        return clean(bx, by, dir)
    else:
        return
    
clean(r, c, d)
cnt = sum(row.count(2) for row in room)
print(cnt)