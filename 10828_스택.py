n = int(input())
stack = []

for i in range(n):
    order = input()
    if "push" in order:
        temp = list(order.split(" "))
        stack.append(temp[1])
    else:
        if "pop" in order:
            if len(stack) > 0:
                print(stack[-1])
                stack.pop()
            else: print("-1")
        elif "size" in order:
            print(len(stack))
        elif "empty" in order:
            if len(stack) > 0:
                print("0")
            else:
                print("1")
        elif "top" in order:
            if len(stack) > 0:
                print(stack[-1])
            else: print("-1")