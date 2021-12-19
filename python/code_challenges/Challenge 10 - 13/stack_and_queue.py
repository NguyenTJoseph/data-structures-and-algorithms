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
        while not self.stackA.is_empty():
            self.stackB.push(self.stackA.pop())
        self.stackB.push(value)

        while not self.stackB.is_empty():
            self.stackA.push(self.stackB.pop())

    def dequeue(self):
        return self.stackA.pop()

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()


    def enqueue(self, name, type):
        if type == "dog":
            self.dogs.enqueue(Animal(name, type))

        if type == "cat":
            self.cats.enqueue(Animal(name, type))


    def dequeue(self, preference):
        if preference == "dog":
            return self.dogs.dequeue().name

        if preference == "cat":
            return self.cats.dequeue().name


def validate_brackets(string):
    opener = Stack()
    closer = Stack()

    for char in string:
        if char == "(" or char == "[" or char == "{":
            opener.push(char)

        if char == ")" or char == "]" or char == "}":
            closer.push(char)

    a = 0
    b = 0
    c = 0

    while not opener.is_empty():
        value = opener.pop()
        if value == "(":
            a += 1
        if value == "[":
            b += 1
        if value == "{":
            c += 1

    while not closer.is_empty():
        value = closer.pop()
        if value == ")":
            a -= 1
        if value == "]":
            b -= 1
        if value == "}":
            c -= 1

    return a == 0 and b == 0 and c == 0
