class Node:
    def __init__(self, data=None, left=None, right=None, key=None):
        self.data = data
        self.left: Node = left
        self.right: Node = right
        self.key = key
