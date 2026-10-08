f = open("input.txt")

stroka = f.readline().split()

stack = []

for i in range(len(stroka)):
    if stroka[i].isdigit():
        stack.append(int(stroka[i]))
    else:
        if stroka[i] == "+":
            result = stack[-2] + stack[-1]
            stack.pop(-1)
            stack.pop(-1)
            stack.append(result)
        elif stroka[i] == "-":
            result = stack[-2] - stack[-1]
            stack.pop(-1)
            stack.pop(-1)
            stack.append(result)
        else:
            result = stack[-2] * stack[-1]
            stack.pop(-1)
            stack.pop(-1)
            stack.append(result)

print(stack[0])