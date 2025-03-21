class ItemExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class Node:
    def __init__(self, data=None, left=None, right=None, key=None):
        self.data = data
        self.left: Node = left
        self.right: Node = right
        self.key = key


class BSTMap:
    def __init__(self):
        self.root: Node = None
        self.size = 0

    def insert(self, key, data):
        """Adds this value pair to the collection"""
        if self.root is None:
            self.root = Node(data=data, key=key)
        elif self.root.key == key:
            raise ItemExistsException()
        elif self.root.right is None and key > self.root.key:
            self.root.right = Node(data=data, key=key)
        elif self.root.left is None and key < self.root.key:
            self.root.left = Node(data=data, key=key)
        else:
            if key > self.root.key:
                return self._insert_helper(self.root.right, key, data)
            if key < self.root.key:
                return self._insert_helper(self.root.left, key, data)
        self.size += 1
        return None

    def _insert_helper(self, node: Node, key, data):
        if node.key == key:
            raise ItemExistsException()
        if key > node.key:
            if node.right is not None:
                return self._insert_helper(node.right, key, data)
            node.right = Node(data=data, key=key)
        if key < node.key:
            if node.left is not None:
                return self._insert_helper(node.left, key, data)
            node.left = Node(data=data, key=key)
        return None

    def update(self, key, data):
        """Sets the data value of the value pair with equal key to data"""
        if self.root is None:
            raise NotFoundException()
        if key > self.root.key:
            return self._update_helper(self.root.right, key, data)
        if key < self.root.key:
            return self._update_helper(self.root.left, key, data)
        return None

    def _update_helper(self, node: Node, key, data):
        if node is None:
            raise NotFoundException()
        if node.key == key:
            node.data = data
        if key > node.key:
            if node.right is not None:
                return self._insert_helper(node.right, key, data)
        elif key < node.key:
            if node.left is not None:
                return self._insert_helper(node.left, key, data)
        return None

    def find(self, key):
        """Returns the data value of the value pair with equal key"""
        if self.root is None:
            raise NotFoundException()
        if key == self.root.key:
            return self.root.data
        if key > self.root.key:
            return self._find_helper(self.root.right, key)
        if key < self.root.key:
            return self._find_helper(self.root.left, key)
        return None

    def _find_helper(self, node: Node, key):
        if node is None:
            raise NotFoundException()
        if key == node.key:
            return node.data
        if key > self.root.key:
            return self._find_helper(node.right, key)
        if key < self.root.key:
            return self._find_helper(node.left, key)
        return None

    def contains(self, key):
        """Returns True if equal key is found in the collection, otherwise False"""
        if key == self.root.key:
            return True
        if key > self.root.key:
            return self._contains_helper(self.root.right, key)
        if key < self.root.key:
            return self._contains_helper(self.root.left, key)
        return False

    def _contains_helper(self, node: Node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key > self.root.key:
            return self._contains_helper(node.right, key)
        if key < self.root.key:
            return self._contains_helper(node.left, key)
        return None

    def remove(self, key):
        """Removes the value pair with equal key from the collection"""
        if not self.contains(key):
            raise NotFoundException()
        self.size -= 1
        if key == self.root.key:
            return self._remove_helper(self.root, key, self.root, "r")
        elif key > self.root.key:
            return self._remove_helper(self.root.right, key, self.root, "r")
        elif key < self.root.key:
            return self._remove_helper(self.root.left, key, self.root, "l")
        return None

    def _remove_helper(self, node: Node, key, prev_node: Node, wrw):
        if key == node.key:
            if node.right is None and node.left is None:
                if wrw == "r":
                    prev_node.right = None
                else:
                    prev_node.left = None
                return
            elif node.right is not None and node.left is not None:
                min_node, min_prev = self._find_min_node(node.right, node)
                if min_node == prev_node.right:
                    # min_prev.right = None
                    prev_node.right = min_prev.right.right
                else:
                    min_prev.left = None
                prev_node.data = min_node.data
                prev_node.key = min_node.key
                return
            else:
                if node.right is None:
                    if wrw == "r":
                        prev_node.right = node.left
                    else:
                        prev_node.left = node.left
                else:
                    if wrw == "r":
                        prev_node.right = node.right
                    else:
                        prev_node.left = node.right
                return
        if key > self.root.key:
            return self._remove_helper(node.right, key, node, "r")
        if key < self.root.key:
            return self._remove_helper(node.left, key, node, "l")

    def _find_min_node(self, node: Node, prev_node: Node):
        if node.left is None:
            return node, prev_node
        return self._find_min_node(node.left, node)

    def __setitem__(self, key, data):
        """Override to allow this syntax -> some_bst_map[key] = data"""
        if not self.contains(key):
            self.insert(key, data)
        else:
            self.update(key, data)

    def __getitem__(self, key):
        """Override to allow this syntax -> my_data = some_bst_map[key]"""
        if not self.contains(key):
            raise NotFoundException()
        return self.find(key)

    def __len__(self):
        """Override to allow this syntax -> length_of_structure = len(some_bst_map)"""
        return self.size

    def __str__(self):
        """Returns a string with the items ordered by key and separated by a single space."""
        ret_str = ""
        helper_ret_str: str = self._print_helper(self.root)
        str_lis = helper_ret_str.strip().split(" ")
        node_lis = []
        for x in str_lis:
            values = list(x.split("|"))
            values[0] = int(values[0])
            node_lis.append(values)
        node_lis.sort()
        for x, y in node_lis:
            x = int(x)
            ret_str += f"{x}:{y} "
        return ret_str

    def _print_helper(self, node: Node):
        if not node:
            return ""
        left = self._print_helper(node.left)
        right = self._print_helper(node.right)

        return f"{node.key}|{node.data} " + left + right

    def count_odd_elements(self):
        if self.root is None:
            return 0
        else:
            if self.root.key % 2 != 0:
                return (
                    1
                    + self._count(self.root.left, dir_v="L")
                    + self._count(self.root.left, dir_v="R")
                    + self._count(self.root.right, dir_v="L")
                    + self._count(self.root.right, dir_v="R")
                )
            return (
                self._count(self.root.left, dir_v="L")
                + self._count(self.root.left, dir_v="R")
                + self._count(self.root.right, dir_v="L")
                + self._count(self.root.right, dir_v="R")
            )

    def _count(self, node, dir_v, count=0):
        if node.key % 2 != 0:
            count += 1
        if node.left and dir_v == "L":
            return self._count(node.left, "L", count)
        if node.left is None and dir_v == "L":
            return count
        if node.right and dir_v == "R":
            return self._count(node.right, "R", count)
        if node.right is None and dir_v == "R":
            return count


class MyComparableKey:
    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __lt__(self, other: object):
        if self.int_value == other.int_value:
            if self.string_value < other.string_value:
                return True
            return False
        if self.int_value < other.int_value:
            return True
        return False


if __name__ == "__main__":
    bst = BSTMap()
    bst.insert(50, "50")
    bst.insert(30, "30")
    bst.insert(20, "20")
    bst.insert(40, "40")
    bst.insert(70, "70")
    bst.insert(60, "60")
    bst.insert(80, "80")
    bst.insert(81, "81")
    print(bst)
    print(bst.count_odd_elements())
