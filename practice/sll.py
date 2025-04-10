class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SLL:
    def __init__(self):
        self.head: Node = Node("Head", None)
        self.size = 0

    def push_back(self, data):
        if self.head.next is None:
            self.head.next = Node(data, None)
        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = Node(data, None)
        self.size += 1

    def push_front(self, data):
        if self.head.next is None:
            self.head.next = Node(data, None)
        else:
            new_node = Node(data, self.head.next)
            self.head.next = new_node
        self.size += 1

    def pop_front(self):
        if self.head.next is None:
            return self.head.next
        ret_value = self.head.next.data
        self.head.next = self.head.next.next
        self.size -= 1
        return ret_value

    def pop_back(self):
        if self.head.next is None:
            return self.head.next
        temp_node = self.head
        while temp_node.next.next is not None:
            temp_node = temp_node.next
        ret_value = temp_node.next
        temp_node.next = None
        self.size -= 1
        return ret_value.data

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        temp_node = self.head.next
        while temp_node is not None:
            ret_str += str(temp_node.data) + " "
            temp_node = temp_node.next
        return ret_str


if __name__ == "__main__":
    sll = SLL()
    sll.push_front("1")
    sll.push_front("2")
    sll.push_front("3")
    sll.push_front("4")
    sll.push_back("0")
    print(sll)
    # print(sll.pop_back())
    # print(sll.pop_front())
