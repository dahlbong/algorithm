import sys
sys.setrecursionlimit(10**6)

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

count_false = 0
count_true = 0

def check_same(x, y, size):
    first_value = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != first_value:
                return False
    return True

def divide_and_conquer(x, y, size):
    global count_false, count_true
    
    if check_same(x, y, size):
        if paper[x][y] == 0:
            count_false += 1
        else:
            count_true += 1
    else:
        new_size = size //2
        divide_and_conquer(x, y, new_size)
        divide_and_conquer(x, y+new_size, new_size)
        divide_and_conquer(x+new_size, y, new_size)
        divide_and_conquer(x+new_size, y+new_size, new_size)
        
divide_and_conquer(0,0,n)

print(count_false)
print(count_true)