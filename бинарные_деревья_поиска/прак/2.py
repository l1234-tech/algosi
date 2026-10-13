from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None


def is_valid_avl(root: Node | None) -> bool:
    def check_avl (node):
        if node is None:
            return -1 

        left = check_avl(node.left)
        if left == -1:
            return -1 

        right = check_avl(node.right)
        if right == -1:
            return -1
        
        if node.left is not None and node.left.key >= node.key:
            return -1
        
        if node.right is not None and node.right.key <= node.key:
            return -1
        
        if abs(left - right) > 1:
            return -1   

        h = max(left, right) + 1
        if node.height != h:
            return -1

    return check_avl(root) != -1