height = []
heightsum = 0
over = 0

for i in range(9):
    height.append(int(input()))

for i in range(9):
    heightsum += height[i]
    
over = heightsum - 100
found = False

for i in range(9):
    for j in range(i+1, 9):
        if height[i] + height[j] == over:
            liar1 = height[i]
            liar2 = height[j]
            found = True
            break
    if found:
        break
            
height.remove(liar1)
height.remove(liar2)
height.sort()
print(*height, sep='\n')