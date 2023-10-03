class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, item):
        node = Node(item)
        self.length += 1
        if self.head == None:
            self.head = node
            return
        node.prev = self.head
        self.head = node

    def pop(self):
        self.length = max(0, self.length - 1)
        if self.length == 0:
            item = self.head
            self.head = None
            return item.value if item else None
        head = self.head
        self.head = head.prev
        return head.value

    def peek(self):
        return self.head.value or None
