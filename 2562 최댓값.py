num = []

index = 1

for i in range(9):
    num.append(int(input()))
    
big = num[0]

for i in range(1,9):
    if big < num[i]:
        big = num[i]
        index = i+1
    else:
        continue
        
print(big, index, sep="\n")