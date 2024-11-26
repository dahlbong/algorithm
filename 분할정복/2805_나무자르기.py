import sys

n, meters = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, sum(trees)

while start <= end:
    mid = (start+end) // 2
    cnt =  0
    
    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    if cnt >= meters:
        start = mid + 1
    else: 
        end = mid - 1
    
print(end)