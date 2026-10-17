from __future__ import annotations


class BTreeNode:
    """Узел B-дерева: ключи и дочерние узлы."""

    def __init__(self, leaf: bool = True) -> None:
        self.leaf = leaf
        self.keys: list[int] = []
        self.children: list[BTreeNode] = []



def process_btree_ops(ops: list[int], t: int = 3) -> list[bool]:
    def new_node(leaf=True):
        return {"keys": [], "children": [], "leaf": leaf}

    root = new_node()
    results = []

    def search(key):
        node = root

        while node is not None:
            i = 0
            while i < len(node["keys"]) and key > node["keys"][i]:
                i += 1

            if i < len(node["keys"]) and node["keys"][i] == key:
                return True

            if node["leaf"]:
                return False

            node = node["children"][i]

        return False

    def split_child(parent, i):
        full = parent["children"][i]
        right = new_node(full["leaf"])

        median = full["keys"][t - 1]
        right["keys"] = full["keys"][t:]
        full["keys"] = full["keys"][:t - 1]

        if not full["leaf"]:
            right["children"] = full["children"][t:]
            full["children"] = full["children"][:t]

        parent["keys"].insert(i, median)
        parent["children"].insert(i + 1, right)

    def insert_nonfull(node, key):
        i = len(node["keys"]) - 1

        if node["leaf"]:
            node["keys"].append(key)

            while i >= 0 and node["keys"][i] > key:
                node["keys"][i + 1] = node["keys"][i]
                i -= 1

            node["keys"][i + 1] = key
            return

        while i >= 0 and key < node["keys"][i]:
            i -= 1
        i += 1

        if len(node["children"][i]["keys"]) == 2 * t - 1:
            split_child(node, i)

            if key > node["keys"][i]:
                i += 1

        insert_nonfull(node["children"][i], key)

    def insert(key):
        nonlocal root

        if search(key):
            return

        if len(root["keys"]) == 2 * t - 1:
            new_root = new_node(False)
            new_root["children"].append(root)
            split_child(new_root, 0)
            root = new_root

        insert_nonfull(root, key)

    for op in ops:
        if op > 0:
            insert(op)
        elif op < 0:
            results.append(search(-op))

    return results
