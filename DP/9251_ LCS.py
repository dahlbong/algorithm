import sys
char_a = list(str(sys.stdin.readline().rstrip()))
char_b = list(str(sys.stdin.readline().rstrip()))

dp=[[0]*(len(char_b)+1) for _ in range(len(char_a)+1)]

for i in range(1, len(char_a)+1):
    for j in range(1, len(char_b)+1):
        if char_a[i-1] == char_b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1]) 