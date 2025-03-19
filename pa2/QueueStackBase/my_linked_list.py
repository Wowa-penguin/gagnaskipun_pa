class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, data):
        if self.head is None:
            self.head = Node(data, self.tail)
            self.tail = self.head
        else:
            new_node = Node(data, self.head)
            if self.size == 1:
                self.tail = self.head
            self.head = new_node
        self.size += 1

    def push_back(self, data):
        if self.head is None:
            self.head = Node(data, self.tail)
            self.tail = self.head
        else:
            node = Node(data, None)
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_front(self):
        if self.head is None or self.size == 0:
            return
        ret = self.head.data
        head = self.head.next
        self.head = head
        self.size -= 1
        return ret

    def pop_back(self):
        if self.head is None or self.size == 0:
            return
        ret_value = 0
        tmp_node = self.head
        if self.size == 1:
            ret_value = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return ret_value
        while tmp_node.next is not None:
            if tmp_node.next.next is not None:
                tmp_node = tmp_node.next
            else:
                ret_value = tmp_node.next.data
                tmp_node.next = None
                self.tail = tmp_node
        self.size -= 1
        return ret_value

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.head
        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

        # ret_str = ""
        # tmp_node = self.head
        # try:
        #     while tmp_node.next is not None:
        #         ret_str += f"{tmp_node.data} "
        #         tmp_node = tmp_node.next
        #     ret_str += f"{tmp_node.data} "
        #     return ret_str
        # except AttributeError:
        #     return ret_str


if __name__ == "__main__":
    lis = LinkedList()
    lis.push_front(1)
    lis.push_front(4)
    lis.push_front(7)
    lis.push_back(3)
    lis.pop_back()
    print(lis)
