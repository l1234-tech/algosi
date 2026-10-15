from dataclasses import dataclass
import sys

f = open("бинарные_деревья_поиска/дз/2 задача/input.txt")

sys.setrecursionlimit(2000)

@dataclass
class Node:
    key: int
    left: "Node" = None
    right: "Node" = None

class BST():
    def __init__(self):
        self.root = None

    def add(self, key: int):
        leave = Node(key)
        if self.root is None:
            self.root = leave
            return 

        else:
            curr = self.root
            while True:
                if key > curr.key:
                    if curr.right != None:
                        curr = curr.right
                    else:

                        curr.right = leave
                        return 
                if key == curr.key:
                    return

                if key < curr.key:
                    if curr.left != None:
                        curr = curr.left
                    else:
                        curr.left = leave
                        return 
    def rotate_left(self, key: int):
        parent = None
        curr = self.root

        while curr is not None and curr.key != key:
            parent = curr 
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        new_child = curr.right
        curr.right = new_child.left
        new_child.left = curr

        if parent is None:
            self.root = new_child
        elif parent.left == curr:
            parent.left = new_child
        else:
            parent.right = new_child

    def rotate_right(self, key: int):
        parent = None
        curr = self.root

        while curr is not None and curr.key != key:
            parent = curr 
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        new_child = curr.left
        curr.left = new_child.right
        new_child.right = curr

        if parent is None:
            self.root = new_child
        elif parent.left == curr:
            parent.left = new_child
        else:
            parent.right = new_child

    def print_node(self):
        if self.root is None:
            print("Empty")
            return
        
        result = []
        def _solve(node: Node):
            if node is not None:
                result.append(str(node.key))
                _solve(node.left)
                _solve(node.right)
        
        _solve(self.root)
        print(" ".join(result))


n = int(f.readline()) 

tree = BST()
keys = list(map(int, f.readline().split()))

for i in range(n):
    tree.add(keys[i])

m = int(f.readline())

for _ in range(m):
    cmd, x  = f.readline().split()
    x = int(x)

    if cmd == "left":
        tree.rotate_left(x)
    else:
        tree.rotate_right(x)

    tree.print_node()