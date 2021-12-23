from Queue import Queue
class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

class kArTree:
    def __init__(self, root=None):
        self.root = root

def fb(node):
    value = ""
    if node.value % 3 == 0:
        value = "Fizz"
    elif node.value % 5 == 0:
        value = "Buzz"
    if node.value % 3 == 0 and node.value % 5 == 0:
        value = "Fizzbuzz"
    if node.value % 3 != 0 and node.value % 5 != 0:
        value = str(node.value)
    return value

def fizzBuzz(tree):
    q = Queue()
    q2 = Queue()
    new = kArTree(Node(fb(tree.root)))
    q2.enqueue(new.root)
    q.enqueue(tree.root)
    while q.front:
        front = q.dequeue()
        parent = q2.dequeue()
        children = []
        print(parent)
        if front.children:
            for node in front.children:
                q.enqueue(node)
                child = Node(fb(node))
                q2.enqueue(child)
                children.append(child)
        parent.children = children
    return new

