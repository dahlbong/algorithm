import sys
from collections import deque
input = sys.stdin.readline

string = list(str(input().rstrip()))
bomb = list(str(input().rstrip()))

newString = []
delString = deque()

def do_delete(x):
    if len(newString) < len(bomb):
        return
    for j in range(len(bomb)-1, -1, -1):
        if x[-1] == bomb[j]:
            delString.appendleft(x.pop(-1))
        else:
            x += delString
            return

for i in range(len(bomb)):
    newString.append(string[i])

for i in range(len(bomb), len(string)):
    if newString[-1] == bomb[-1]:
        do_delete(newString)
        delString = deque()
    newString.append(string[i])

do_delete(newString)

if len(newString) == 0:
    print('FRULA')
else:
    print(*newString, sep='')

# 매우 헤맴
# 1) 스택 발상 늦게 떠오름
# 2) newString에 전체 string을 삽입 완료한 후에도 do_delete() 함수 실행 필요하다는 생각이 늦게 떠오름