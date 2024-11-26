n = int(input())
ans = 0

check_y = [0] * n
check_diag1 = [0]*(2*n)
check_diag2 = [0]*(2*n)

def n_queen(y):
    global ans
    if y == n:
        ans += 1
        return
    for i in range(n):
        if check_y[i] == check_diag1[y+i] == check_diag2[y-i] == 0:
            check_y[i] = check_diag1[y+i] = check_diag2[y-i] = 1
            n_queen(y+1)
            check_y[i] = check_diag1[y+i] = check_diag2[y-i] = 0

n_queen(0)
print(ans)