n = int(input())
arr=[]

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
        
print(arr)

flag = []*n

for i in range(n):
    for j in range(n):
        if arr[i][j] 