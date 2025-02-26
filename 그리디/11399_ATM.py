import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort()
dp = [times[0]] + [0 for _ in range(N-1)]

if N == 1:
    print(times[0])
    exit()

for i in range(1, len(times)):
    dp[i] = dp[i-1] + times[i]

print(sum(dp))