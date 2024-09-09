from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    order = input().strip()
    if order.startswith("push"):
        _, value = order.split()
        queue.append(value)
    elif order == "pop":
        if queue:
            print(queue.popleft())
        else: print("-1")
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        print("0" if queue else "1")
    elif order == "front":
        print(queue[0] if queue else "-1")
    elif order == "back":
        print(queue[-1] if queue else "-1")