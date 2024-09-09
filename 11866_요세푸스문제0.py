import sys
from collections import deque

input = sys.stdin.readline
result = []

n, k = map(int, input().split(" "))
queue = deque(range(1, n+1))

while queue:
    queue.rotate(-(k-1))
    result.append(queue.popleft())
    
print(f"<{', '.join(map(str, result))}>")