f = open("input.txt")
pushed = list(map(int, f.readline().split()))
popped = list(map(int, f.readline().split()))

stack = []
j = 0
for x in pushed:
    stack.append(x)
    while stack and stack[-1] == popped[j]:
        stack.pop()
        j += 1

print(j == len(popped))