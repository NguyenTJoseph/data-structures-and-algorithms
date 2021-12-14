class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class InvalidOperationError(Exception):
    pass

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        top = self.top
        if top:
            self.top = Node(value, top)
        self.top = Node(value, top)

    def pop(self):

        if not self.top:
            raise InvalidOperationError(
                "Not allowed on empty collection"
            )
        pop = self.top
        self.top = self.top.next
        return pop.value

    def peek(self):

        if not self.top:
            raise InvalidOperationError(
                "Not allowed on empty collection"
            )

        return self.top.value

    def is_empty(self):
        return self.top is None


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

class PseudoQueue:
    def __init__(self):
        self.stackA = Stack()
        self.stackB = Stack()

    def enqueue(self, value):
        empty = self.stackB
        self.stackB.push(value)
        if self.stackA.top != None:
            self.stackB.push(self.stackA.pop())
        self.stackA = self.stackB
        self.stackB = empty

    def dequeue(self):
        return self.stackA.pop()
