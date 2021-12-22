class InvalidOperationError(Exception):
    pass

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self, front=None):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear:
            self.rear.next = node
        else:
            self.front = node
        self.rear = node

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError(
                "Not allowed on empty collection"
            )
        node = self.front
        if node == self.rear:
            self.rear = None
        else:
            self.front = self.front.next
            node.next = None
        return node.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError(
                "Not allowed on empty collection"
            )
        return self.front.value

    def is_empty(self):
        return self.front is None
