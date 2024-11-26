
import sys

n = int(sys.stdin.readline())
move = []

# def hanoi(disk, start, end):
#     move = 0
#     moves = []
#     move, moves = hanoi_sub(disk, start, end, 2, move, moves)
#     print(move)
#     print(*moves, sep='\n')
    

# def hanoi_sub(x, start, end, temp, move, moves):
#     if x == 1:
#         move += 1
#         moves.append("1 3")
#     else:
#         move, moves = hanoi_sub(x - 1, start, temp, end, move, moves)
#         move += 1
#         moves.append(f"{start} {end}")
#         move, moves = hanoi_sub(x - 1, temp, end, start, move, moves)
#     return move, moves

def hanoi(disk, start, temp, end):
    if disk == 1:
        move. append([start, end])
    else:
        hanoi(disk-1, start, end, temp)
        move. append([start, end])
        hanoi(disk-1, temp, start, end)

if n <= 20 :
    hanoi(n, 1, 2, 3)
    len = len(move)
    print(len)
    for i in range(len):
        print(*move[i])
else:
    print(2**n-1)   





