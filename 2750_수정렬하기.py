n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

for j in range(len(arr)):
    min_index = j
    for k in range(j+1, len(arr)):
        if arr[min_index] > arr[k]:
            min_index = k
    arr[j], arr[min_index] = arr[min_index], arr[j]
        
print(*arr, sep='\n')