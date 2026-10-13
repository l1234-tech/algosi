from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None

def delete_node(root: Node | None, key: int) -> Node | None:
    if root is None:
        return None

    if key < root.key:
        root.left = delete_node(root.left, key)

    elif key > root.key:
        root.right = delete_node(root.right, key)

    else:
        if root.left is None and root.right is None:
            return None

        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        successor = root.right

        while successor.left is not None:
            successor = successor.left

        root.key = successor.key

        root.right = delete_node(root.right, successor.key)

    return root
