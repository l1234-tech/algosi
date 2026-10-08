f = open("input.txt")
Q = int(f.readline())

class Deque:
    def __init__(self, cap):
        self.data = [0] * cap
        self.cap = cap
        self.head = 0      
        self.tail = 0      
        self.count = 0 

    def push_back(self, x):
        self.data[self.tail] = x
        self.tail = (self.tail + 1) % self.cap
        self.count += 1
        

    def push_front(self, x):
        self.head = (self.head - 1) % self.cap
        self.data[self.head] = x
        self.count += 1

    def pop_back(self):
        if self.count == 0:
            return "Error"
        else:
            self.tail = (self.tail - 1) % self.cap
            last = self.data[self.tail]
            self.count -= 1
            return last
        
    def pop_front(self):
        if self.count == 0:
            return "Error"
        else:
            first = self.data[self.head]
            self.head = (self.head + 1) % self.cap
            self.count -= 1
            return first

    def get_back(self):
        if self.count == 0:
            return "Error"
        else:
            return self.data[self.tail - 1]

    def get_front(self):
        if self.count == 0:
            return "Error"
        else:
            return self.data[self.head]

    def size(self):
        return self.count

deque = Deque(Q + 1)  

for _ in range(Q):
    stroka = f.readline().split()
    cmd = stroka[0]
    if cmd == "push":
        if stroka[1] == "back":
            deque.push_back(stroka[2])
        else:
            deque.push_front(stroka[2])
    elif cmd == "pop":
        if stroka[1] == "back":
            print(deque.pop_back())
        else:
            print(deque.pop_front())
    elif cmd == "get":
        if stroka[1] == "back":
            print(deque.get_back())
        else:
            print(deque.get_front())
    else:
        print(deque.size())