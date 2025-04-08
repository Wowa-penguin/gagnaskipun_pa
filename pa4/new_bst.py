from random import Random
from node import Node
from error import NotFoundException, ItemExistsException


class BTSMap:
    def __init__(self):
        self.root: Node = None
        self.size = 0

    def insert(self, key: int, data):
        if self.root is None:
            self.root = Node(data=data, key=key)
        else:
            self._insert(self.root, key, data)
            self.size += 1

    def _insert(self, node: Node, key: int, data):
        if node.key == key:
            raise ItemExistsException
        if node.key > key:
            if node.left is None:
                node.left = Node(data=data, key=key)
            else:
                return self._insert(node.left, key, data)
        else:
            if node.right is None:
                node.right = Node(data=data, key=key)
            else:
                return self._insert(node.right, key, data)

    def update(self, key: int, data):
        if self.root is None:
            raise NotFoundException
        self._update(self.root, key, data)

    def _update(self, node: Node, key: int, new_data):
        if node.key == key:
            node.data = new_data
            return
        if node.key > key and node.left is not None:
            return self._update(node.left, key, new_data)
        if node.key < key and node.right is not None:
            return self._update(node.right, key, new_data)
        raise NotFoundException

    def find(self, key: int):
        if self.root is None:
            raise NotFoundException
        return self._find(self.root, key)

    def _find(self, node: Node, key: int):
        if node.key == key:
            return node.data
        if node.key > key and node.left is not None:
            return self._find(node.left, key)
        if node.key < key and node.right is not None:
            return self._find(node.right, key)
        raise NotFoundException

    def contains(self, key: int):
        try:
            self._find(self.root, key)
            return True
        except NotFoundException:
            return False

    def remove(self, key: int):
        if self.root is None:
            raise NotFoundException
        self._remove(self.root, self.root, key)
        self.size -= 1

    def _remove(self, node: Node, prev_node: Node, key: int):
        if node.key == key:
            if node.left is None and node.right is None:
                if prev_node.left is not None and prev_node.left.key == key:
                    prev_node.left = None
                else:
                    prev_node.right = None
                return
            if node.left is None or node.right is None:
                child_node = self._one_child(node)
                if prev_node.left is not None and prev_node.left.key == key:
                    prev_node.left = child_node
                else:
                    prev_node.right = child_node
            else:
                last_node, prev_last_node = self._two_child(node, node, node.key)
                node.key = prev_last_node.key
                node.data = prev_last_node.data
                prev_last_node.key = last_node.key
                prev_last_node.data = last_node.data
                prev_last_node.left = None
                prev_last_node.right = None
            return

        if node.key > key and node.left is not None:
            return self._remove(node.left, node, key)
        if node.key < key and node.right is not None:
            return self._remove(node.right, node, key)
        raise NotFoundException

    def _one_child(self, node: Node):
        if node.left is None:
            return node.right
        return node.left

    def _two_child(self, node: Node, prev_node: Node, key):
        if node.left is None and node.right is None:
            return node, prev_node
        if node.left is not None and node.left.key > key:
            return self._two_child(node.left, node, key)
        return self._two_child(node.right, node, key)

    def __setitem__(self, key, data):
        if not self.contains(key):
            self.insert(key, data)
        else:
            self.update(key, data)

    def __getitem__(self, key):
        if not self.contains(key):
            raise NotFoundException()
        return self.find(key)

    def __len__(self):
        return self.size

    def __str__(self):
        items = []

        def in_order(node):
            if node:
                in_order(node.left)
                items.append(f"{{{node.key}:{node.data}}}")
                in_order(node.right)

        in_order(self.root)
        return " ".join(items)


def get_random_key():
    ran = Random()
    return ran.randint(0, 1000)


if __name__ == "__main__":
    bts = BTSMap()
    print(bts)
    key_to_update = get_random_key()
    key_to_find = get_random_key()
    bts.insert(get_random_key(), "Root Node")
    bts.insert(get_random_key(), "1")
    bts.insert(key_to_update, "2")
    bts.insert(20, "Remove me plis")
    bts.insert(21, "remove right")
    bts.insert(19, "Remove left")
    bts.insert(key_to_find, "find me plis")
    bts.update(key_to_update, "New data update")
    print(bts.find(key_to_find))
    print(bts.contains(key_to_find))
    bts.remove(20)
    print(bts)
