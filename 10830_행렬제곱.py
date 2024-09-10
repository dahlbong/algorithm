n,b = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

#행렬 제곱 함수
def matmul(n, mat1, mat2):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000
    return result

#분할 정복 함수
def divide(n, b, mat):
    if b == 1:
        return mat
    elif b == 2:
        return matmul(n, mat, mat)
    else:
        tmp = divide(n, b//2, mat)
        if b%2 == 0:
            return matmul(n, tmp, tmp) 
        else:
            return matmul(n, matmul(n, tmp, tmp), mat)
        
result = divide(n, b, a)

for i in range(n):
    print(*map(lambda x: x%1000, result[i]), end=' ')
    print()