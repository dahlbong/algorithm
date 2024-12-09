import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (i + 3) for i in range(n)]
dp[0] = [0] + triangle[0] + [0]

if n == 1:
    print(max(triangle[0]))
    exit()

for i in range(len(dp)):
    for j in range(1, len(dp[i])-1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j-1]
    
print(max(dp[-1]))