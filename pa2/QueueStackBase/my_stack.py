from array_deque import ArrayDeque


class Stack:
    def __init__(self):
        self.container = ArrayDeque()

    def push(self, data):
        self.container.push_back(data)

    def pop(self):
        return self.container.pop_back()

    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return f"{self.container}"


if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(7)
    print("the data structure is of size: " + str(stack.get_size()))
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print("the data structure is of size: " + str(stack.get_size()))
