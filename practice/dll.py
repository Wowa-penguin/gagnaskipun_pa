class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DLL:
    def __init__(self):
        self.head = Node("Head", None, None)
        self.tail = Node("tail", None, None)
        self.curr = self.head
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, data):
        if self.curr == self.head:
            self.curr = Node(data, self.tail, self.head)
            self.head.next = self.curr
            self.tail.prev = self.curr
        else:
            new_node = Node(data, self.curr.next, self.curr)
            self.curr.next.prev = new_node
            self.curr.next = new_node
            self.curr = new_node
        self.size += 1

    def remove(self):
        if self.curr == self.head:
            return
        new_curr = self.curr.prev
        self.curr.prev.next = self.curr.next
        self.curr.next.prev = self.curr
        self.curr = new_curr
        self.size -= 1

    def get_data(self):
        return self.curr.data

    def move_to_next(self):
        if self.curr.next == self.tail:
            return
        self.curr = self.curr.next

    def move_to_prev(self):
        if self.curr.prev == self.head:
            return
        self.curr = self.curr.prev

    def __str__(self):
        ret_str = ""
        temp_node = self.head.next
        while temp_node != self.tail:
            ret_str += str(temp_node.data) + " "
            temp_node = temp_node.next
        return ret_str

    def move_to_pos(self, index):
        if index < self.size < index:
            return
        temp_node = self.head.next
        for x in range(self.size):
            if x == index:
                self.curr = temp_node
                break
            temp_node = temp_node.next

    def clear(self):
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.head

    def get_first_node(self):
        return self.head.next

    def get_last_node(self):
        return self.tail.prev


if __name__ == "__main__":
    dll = DLL()
    dll.insert("1")
    dll.insert("2")
    dll.insert("3")
    dll.insert("4")
    dll.insert("5")
    print(dll.get_data())
    print(dll)
