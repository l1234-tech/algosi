f = open("input.txt")
Q = int(f.readline())

class Queue():
    def __init__(self):
        self.queue = []
        self.head = 0

    def push(self, x):
        self.queue.append(x)

    def size(self):
        return (len(self.queue) - self.head)

    def get(self):
        if self.head >= len(self.queue):
            return "Error"
        else:
            return self.queue[self.head]

    def pop(self):
        if self.head >= len(self.queue):
            return "Error"
        else:
            result = self.queue[self.head]
            self.head += 1
            return result

stack = Queue()

for _ in range(Q):
    stroka = f.readline().split()
    if stroka[0] == "push":
        stack.push(stroka[1])
    elif stroka[0] == "pop":
        print(stack.pop())
    elif stroka[0] == "size":
        print(stack.size())
    else:
        print(stack.get())