class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def prepend(self, item):
        self.length += 1
        if self.length == 1:
            self.head = self.tail = Node(item)
            return
        old_head = self.head
        self.head = Node(item)
        self.head.next = old_head
        old_head.prev = self.head

    def insert_at(self, item, index):
        if index == 0:
            return self.prepend(item)
        if index == self.length - 1:
            return self.append(item)
        curr = self.get(index)
        curr_prev = self.get(index - 1)
        curr_prev.next = Node(item)
        curr_prev.next.next = curr

    def append(self, item):
        self.length += 1
        if self.length == 1:
            self.head = self.tail = Node(item)
            return
        old_tail = self.tail
        self.tail = Node(item)
        old_tail.next = self.tail

    def remove(self, item):
        n = self.head
        i = 0
        while i < self.length:
            if n.value == item:
                return self.remove_at(i)
            n = n.next
            i += 1
        return None

    def get(self, idx):
        return self.get_at(idx).value

    def get_at(self, idx):
        if idx > self.length - 1:
            return None

        n = self.head
        i = 0
        while i < idx:
            n = n.next
            i += 1
        return n

    def remove_at(self, idx):
        i = 0
        n = self.head
        while n:
            if i == idx:
                if i > 0:
                    prev_node = self.get_at(i - 1)
                    prev_node.next = prev_node.next.next
                else:
                    self.head = n.next
                self.length -= 1
                return n.value
            i += 1
            n = n.next
        return None

