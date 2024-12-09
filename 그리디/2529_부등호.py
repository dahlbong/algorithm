import copy

k = int(input())
largeString = list(str(input().replace(" ", "")))
largeString.append(largeString[-1]) 
smallString = copy.deepcopy(largeString)

largeNum = []
smallNum = []
nums = []

def getNum(stringType, numType, front, back, dir):
    tempNums = []
    cur = stringType.pop(0)
    if cur == back:
        tempNums = [nums.pop(0)]
    else:
        numType = [nums.pop(0)]

    while stringType:
        before = cur
        cur = stringType.pop(0)
        tempNums.append(nums.pop(0))
        if cur == back or (cur == back and before == front):
            continue
        elif cur == front :
            while tempNums:
                numType.append(tempNums.pop(-1))
    while tempNums:
        numType.append(tempNums.pop(-1))

    return numType

[nums.append(i) for i in range(9, 8 - k, -1)]
print(*getNum(largeString, largeNum, '>', '<', -1), sep="")

[nums.append(i) for i in range(k + 1)]
print(*getNum(smallString, smallNum, '<', '>', 0), sep="")


# 뻘짓 레전드.. 또 stack 도입할 생각 못해서 뻘짓하다가 시간 다써먹음
# 앞뒤만 삽입/삭제하는 문제는 스택 생각하자 ㅈㅂㅈㅂㅈㅂㅈㅂㅈㅂ
# 처음에 최소값과 최대값을 구하는 매커니즘은 동일하니 함수로 구현하자 생각했는데, 은근 함수로 바꾸다가 시간을 많이 써먹었다.
# 코테는 답만 맞추면 된다. 시간이 걸릴 것 같은 리팩토링은 자제하자.