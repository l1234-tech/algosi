from dataclasses import dataclass
import sys

f = open("бинарные_деревья_поиска/дз/1 задача/input.txt")

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

    def delete(self, key):
        def _delete_recursive(node: Node, key):
            if node is None:
                return None
            
            if key < node.key:
                node.left = _delete_recursive(node.left, key)
            elif key > node.key:
                node.right = _delete_recursive(node.right, key)
            else:
                if node.left is None and node.right is None:
                    return None
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                
                node.key = successor.key
                node.right = _delete_recursive(node.right, successor.key)
            
            return node

        self.root = _delete_recursive(self.root, key)            

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
        def get_height(node: Node):
            if node is None:
                return 0
            return 1 + max(get_height(node.left) , get_height(node.right))

        return (get_height(self.root))


n = int(f.readline())

tree = BST()
for s in f:
    cmd = [x for x in s.split()]
    if len(cmd) == 2:
        if cmd[0] == "add":
            tree.add(int(cmd[1]))
        elif cmd[0] == "del":
            tree.delete(int(cmd[1]))
        elif cmd[0] == "exists":
            if tree.exists(int(cmd[1])):
                print("YES")
            else:
                print("NO")
    else:
        if cmd[0] == "height":
            print(tree.height())
        else:
            tree.print_node()