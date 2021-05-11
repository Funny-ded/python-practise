x = input()
stack = []
while x != '=':
    if x == '+':
        stack.append(stack.pop(-2) + stack.pop(-1))
    elif x == '*':
        stack.append(stack.pop(-2) * stack.pop(-1))
    elif x == '-':
        stack.append(stack.pop(-2) - stack.pop(-1))
    else:
        stack.append(int(x))
    x = input()
print(stack[0])
