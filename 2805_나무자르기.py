import sys

n, meters = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

get = 0

for height in range(max(trees), 0, -1):
    for i in range(n):
        if trees[i] > height:
            get += trees[i] - height
        else:
            continue
    if get >= meters:
        print(height)
        break
    else:
        get = 0