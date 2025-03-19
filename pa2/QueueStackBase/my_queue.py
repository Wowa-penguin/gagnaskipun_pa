from my_linked_list import LinkedList


class Queue:
    def __init__(self):
        self.container = LinkedList()

    def add(self, data):
        self.container.push_front(data)

    def remove(self):
        return self.container.pop_back()

    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return f"{self.container}"


if __name__ == "__main__":
    queue = Queue()
    queue.add(2)
    queue.add(4)
    queue.add(7)
    print("the data structure is of size: " + str(queue.get_size()))
    print(queue.remove())
    print(queue.remove())
    print(queue.remove())
    print(queue.remove())
    print("the data structure is of size: " + str(queue.get_size()))
