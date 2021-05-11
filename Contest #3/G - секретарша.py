data = list(input().split())
stack = []
for i in range(len(data)):
    if data[i] == '#':
        stack.append(sum(stack))
        for j in range(len(stack) - 1):
            stack.pop(0)
    elif data[i] == '%':
        if len(stack) < 2:
            stack.append(0)
            break
        else:
            stack.append(stack[-2] * stack[-1] / 100)
            for j in range(2):
                stack.pop(-2)
    else:
        stack.append(int(data[i]))
print(float(stack[-1]))
