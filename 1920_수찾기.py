n = int(input())
arr_n = list(map(int, input().split()))

m = int(input())
arr_m = list(map(int,input().split()))

# arr_n.sort()


# bit_arr_n = [False for _ in range(max(arr_m))]
# bit_arr_m = [False for _ in range(max(arr_m))]

# for i in arr_n:
#     bit_arr_n[i-1] = True
    
# for i in arr_m:
#     bit_arr_m[i-1] = True

# for i in arr_m:
#     if bit_arr_n[i-1] == bit_arr_m[i-1]:
#         print("1")
#     else:
#         print("0")

set_n = set(arr_n)
count = 0

for i in arr_m:
    if i in set_n:
        print("1")
        count += 1
    else:
        print("0")
        count += 1
    if count == len(arr_m):
        break