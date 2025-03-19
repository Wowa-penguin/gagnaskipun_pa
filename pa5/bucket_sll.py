from node import Node
from error import ItemExistsException, NotFoundException


class Bucket:
    def __init__(self):
        self.head: Node = Node(None, None)
        self.size = 0

    def insert(self, key, data):
        if self.head.next is None:
            self.head.next = Node(key, data, None)
        else:
            temp_node: Node = self.head.next
            while temp_node:
                if temp_node.key == key:
                    raise ItemExistsException
                if temp_node.next is None:
                    temp_node.next = Node(key, data, None)
                    break
                temp_node = temp_node.next
        self.size += 1

    def update(self, key, data):
        temp_node: Node = self.head.next
        while temp_node:
            if temp_node.key == key:
                temp_node.data = data
                return
            temp_node = temp_node.next
        raise NotFoundException

    def find(self, key):
        temp_node: Node = self.head.next
        while temp_node:
            if temp_node.key == key:
                return temp_node.data
            temp_node = temp_node.next
        raise NotFoundException

    def contains(self, key):
        try:
            if self.find(key):
                return True
        except NotFoundException:
            return False

    def remove(self, key):
        temp_node: Node = self.head
        while temp_node.next:
            if temp_node.next.key == key:
                temp_node.next = temp_node.next.next
                return
            temp_node = temp_node.next
        raise NotFoundException

    def __setitem__(self, key, data):
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.size


if __name__ == "__main__":
    sll = Bucket()
