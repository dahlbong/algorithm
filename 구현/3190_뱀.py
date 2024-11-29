import sys
from collections import deque
input = sys.stdin.readline

board = int(input())
apples = [tuple(map(int, input().split())) for _ in range(int(input()))]
rotates = [tuple(map(str, input().split())) for _ in range(int(input()))]

snake = [(1, 1)]
time = 0

curPosition = (1, 1)
direction = 0
movingStandard = [(0, 1), (1, 0), (0, -1), (-1, 0)]       # 0, 1, 2, 3
getL= [(-1, 0), (0, 1), (1, 0), (0, -1)]    # 3, 0, 1, 2
getD = [(1, 0), (0, -1), (-1, 0), (0, 1)]   # 1, 2, 3, 0

def getDirection(direction):
    if len(rotates) == 0 or int(rotates[0][0]) != time:
        return movingStandard[direction], direction
    elif rotates[0][1] == 'D':
        rotates.pop(0)
        retVal = getD[direction]
        direction = movingStandard.index(retVal)
        return retVal, direction
    elif rotates[0][1] == 'L':
        rotates.pop(0)
        retVal = getL[direction]
        direction = movingStandard.index(retVal)
        return retVal, direction
while (1 <= curPosition[0] <= board and 1 <= curPosition[1] <= board):
    moving, direction = getDirection(direction)
    curPosition = (curPosition[0] + moving[0], curPosition[1] + moving[1])

    if curPosition in snake:
        print(time + 1)
        exit()
    
    snake.append(curPosition)
    if curPosition not in apples:
        snake.pop(0)
    else:
        apples.remove(curPosition) 
    time += 1

print(time)
