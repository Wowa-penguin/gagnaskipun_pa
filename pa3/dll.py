class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.size = 0
        self.position = self.tail

        self.tail.prev = self.head
        self.head.next = self.tail

    def insert(self, data):
        """Inserts an item with that value in front of the node at the current position"""
        new_node = Node(data, prev=self.position.prev, next=self.position)
        self.position.prev.next = new_node
        self.position.prev = new_node
        self.position = self.position.prev
        self.size += 1

    def remove(self):
        """Removes the node at the current position if there is one (otherwise does nothing)x"""
        if self.position == self.tail or self.position == self.head:
            return
        if self.head.next is None:
            return
        self.position.prev.next = self.position.next
        self.position.next.prev = self.position.prev
        self.position = self.position.next
        self.size -= 1

    def get_value(self):
        """Returns the value of the item at the current position in the list (None if not item)"""
        if self.size == 0:
            return None
        return self.position.data

    def move_to_next(self):
        """Moves the current position one item closer to the tail/trailer"""
        if self.position == self.tail:
            return
        self.position = self.position.next

    def move_to_prev(self):
        """Moves the current position one item closer to the head/header"""
        if self.position.prev == self.head:
            return
        self.position = self.position.prev

    def move_to_pos(self, pos):
        """Moves the current position to item #position in the list"""
        if (self.size + 1) > pos >= 0:
            self.position = self.head
            for _ in range(pos + 1):
                self.position = self.position.next
        else:
            return

    def clear(self):
        """Clears all nodes from the list"""
        self.head.next = self.tail
        self.tail.prev = self.head
        self.position = self.tail
        self.size = 0

    def get_first_node(self):
        """Returns the first Node of the list"""
        if self.size == 0:
            return None
        return self.head.next

    def get_last_node(self):
        """Returns the last Node of the list"""
        if self.size == 0:
            return None
        return self.tail.prev

    def partition(self, low: Node, high: Node):
        """Takes in two nodes from the list as a parameter"""
        if self.size == 0:
            return None

        self.position = low.next
        while self.position != self.tail:
            if self.position.data < low.data:
                tmp_data = self.position.data
                self.remove()
                self.position = low
                self.insert(tmp_data)
                self.position = low.next
            else:
                self.position = self.position.next
        self.position = low

    def sort(self):
        """Orders the items in the list"""
        if self.size == 0:
            return None
        count = 0
        self.position = self.head.next
        while self.position.next != self.tail:
            if self.position.data > self.position.next.data:
                tmp_data = self.position.next.data
                self.position = self.position.next
                self.remove()
                self.position = self.position.prev
                self.insert(tmp_data)
                self.position = self.head.next
                count += 1
                print(count)
            else:
                self.position = self.position.next
        self.position = self.head.next

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        tmp_node = self.head.next
        try:
            while tmp_node.next is not None:
                if tmp_node is not None:
                    ret_str += f"{tmp_node.data} "
                tmp_node = tmp_node.next
            return ret_str
        except AttributeError:
            return ret_str


if __name__ == "__main__":
    dll_lis = DLL()
    dll_lis.insert(6)
    dll_lis.remove()
    # for _ in range(1000):
    #     dll_lis.insert(random.randint(5, 50))

    # dll_lis.sort()
    print(dll_lis)
