class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def preOrder(self):
        values = []
        def walk(root):
            if root is None:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)
        walk(self.root)

        return values

    def inOrder(self):
        values = []
        def walk(root):
            if root is None:
                return
            walk(root.left)
            values.append(root.value)
            walk(root.right)
        walk(self.root)

        return values

    def postOrder(self):
        values = []
        def walk(root):
            if root is None:
                return
            walk(root.left)
            walk(root.right)
            values.append(root.value)
        walk(self.root)

        return values

    def findMax(self):

        def walk(root):
            rootVal = root.value
            if root.left:
                left = walk(root.left)
                if (left.value > rootVal):
                    root = left
            if root.right:
                right = walk(root.right)
                if (right.value > rootVal):
                    root = right


            return root
        return walk(self.root).value

class BinarySearchTree(BinaryTree):
    def add(self, value):
        node = Node(value)
        def walk(root, to_add):
            if to_add.value < root.value:
                if root.left:
                    walk(root.left, to_add)
                else:
                    root.left = to_add
            else:
                if root.right:
                    walk(root.right, to_add)
                else:
                    root.right = to_add

        if self.root is None:
            self.root = node
        else:
            walk(self.root, node)

    def contains(self, value):
        status = False
        def walk(root):
            if root and root.value == value:
                nonlocal status
                status = True
            if root is None:
                return
            walk(root.left)
            walk(root.right)


        walk(self.root)
        return status

from Queue import Queue
def breadth_first(tree):
    list = []
    breadth = Queue()
    breadth.enqueue(tree.root)
    while breadth.front:
        print("pass")
        front = None
        front = breadth.dequeue()
        list.append(front.value)

        if front.left:
            breadth.enqueue(front.left)

        if front.right:
            breadth.enqueue(front.right)
    list.pop()
    return list
