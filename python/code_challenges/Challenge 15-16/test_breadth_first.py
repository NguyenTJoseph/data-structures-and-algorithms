from tree import breadth_first, BinaryTree, Node


def test_breadth_firstA():
    tree = BinaryTree(Node(1))
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.right.right = Node(5)
    actual = breadth_first(tree)
    expected = [1,2,3,4,5]
    assert actual == expected

def test_breadth_firstB():
    tree = BinaryTree(Node(2))
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    actual = breadth_first(tree)
    expected = [2,7,5,2,6,9,5,11,4]
    assert actual == expected
