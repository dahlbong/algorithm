import sys
from bisect import bisect_left

input = sys.stdin.readline

hunter, animal, aim = map(int, input().split(' '))
hunters = list(map(int, input().split()))
animals = [list(map(int, input().split())) for _ in range(animal)]

result = 0
hunters.sort()

for x, y in animals:
    idx = bisect_left(hunters, x) #x값 기준으로 가장 가까운 사냥꾼의 인덱스
    nearest_dist = float('inf') #float('inf'): 양의 무한대 표현식
    if idx < len(hunters):
        nearest_dist = min(nearest_dist, abs(hunters[idx] - x) + y)
        
    if idx > 0:
        nearest_dist = min(nearest_dist, abs(hunters[idx-1] - x) + y)
        
    if nearest_dist <= aim:
        result += 1
        
print(result)
  