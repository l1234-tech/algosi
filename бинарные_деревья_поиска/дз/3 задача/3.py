from dataclasses import dataclass
import sys


f = open("бинарные_деревья_поиска/дз/3 задача/input.txt")

sys.setrecursionlimit(2000)

@dataclass
class AVLNode:
    key: int
    left: "AVLNode" = None
    right: "AVLNode" = None
    height: int = 0

class AVL():
    def __init__(self):
        self.root = None

    def height_node(self, node: AVLNode):
        if node is None:
            return -1
        else:
            return node.height
        
    def balance_factor(self, node: AVLNode) -> int:
        return self.height_node(node.left) - self.height_node(node.right)
    
    def update(self, node: AVLNode) -> None:
        node.height = 1 + max(self.height_node(node.left), self.height_node(node.right))

    def rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        assert x is not None
        y.left = x.right
        x.right = y
        self.update(y)
        self.update(x)
        return x

    def rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        assert y is not None
        x.right = y.left
        y.left = x
        self.update(x)
        self.update(y)
        return y

    def avl_insert(self, root: AVLNode | None, key: int) -> AVLNode:
        if root is None:
            return AVLNode(key)
        
        if key == root.key:
            return root
        
        if key < root.key:
            root.left = self.avl_insert(root.left, key)
        else:
            root.right = self.avl_insert(root.right, key)
        self.update(root)
        bf = self.balance_factor(root)
        # LL
        if bf > 1 and key < root.left.key:  
            return self.rotate_right(root)
        # RR
        if bf < -1 and key > root.right.key:  
            return self.rotate_left(root)
        # LR
        if bf > 1 and key > root.left.key:  
            root.left = self.rotate_left(root.left)  
            return self.rotate_right(root)
        # RL
        if bf < -1 and key < root.right.key:  
            root.right = self.rotate_right(root.right)  
            return self.rotate_left(root)
        return root           

    def print_node(self):
        if self.root is None:
            print("Empty")
            return
        
        result = []
        def _solve(node: AVLNode):
            if node is not None:
                result.append(str(node.key))
                _solve(node.left)
                _solve(node.right)
        
        _solve(self.root)
        print(" ".join(result))

    def print_root(self):
        res = self.root
        if res is None:
            print("Empty")
        else:
            print(res.key)

    def exists(self, key):
        curr = self.root

        while curr is not None:
            if key == curr.key:
                return True
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def height(self):
        return self.height_node(self.root) + 1


n = int(f.readline())

tree = AVL()
for _ in range(n):
    cmd = f.readline().split()

    if cmd[0] == "add":
        tree.root = tree.avl_insert(tree.root, int(cmd[1]))

    elif cmd[0] == "exists":
        print("YES" if tree.exists(int(cmd[1])) else "NO")

    elif cmd[0] == "root":
        tree.print_root()

    elif cmd[0] == "height":
        print(tree.height())

    elif cmd[0] == "print":
        tree.print_node()