from tree import Node, BinaryTree, BinarySearchTree

def test_instantiate():
    assert BinaryTree()

def test_instantiate_with_root():
    a = Node("a")
    tree = BinaryTree(a)
    actual = tree.root.value
    expected = "a"
    assert actual == expected

def test_left_right():
    a = Node("a")
    a.left = Node("b")
    a.right = Node("c")
    tree =  BinaryTree(a)
    actual = (tree.root.value + tree.root.left.value + tree.root.right.value)
    expected = "abc"
    assert actual == expected

def test_pre_order():
    a = Node("a")
    a.left = Node("b")
    a.right = Node("c")
    tree =  BinaryTree(a)
    actual = tree.preOrder()
    expected = ["a", "b", "c"]
    assert actual == expected

def test_in_order():
    a = Node("a")
    a.left = Node("b")
    a.right = Node("c")
    tree =  BinaryTree(a)
    actual = tree.inOrder()
    expected = ["b", "a", "c"]
    assert actual == expected

def test_post_order():
    a = Node("a")
    a.left = Node("b")
    a.right = Node("c")
    tree =  BinaryTree(a)
    actual = tree.postOrder()
    expected = ["b", "c", "a"]
    assert actual == expected

def test_binary_search_add_one():
    search = BinarySearchTree()
    search.add("a")
    actual = search.root.value
    expected = "a"
    assert actual == expected

def test_binary_search_add_multiple():
    search = BinarySearchTree()
    search.add("b")
    search.add("a")
    search.add("c")
    actual = (search.root.value + search.root.left.value + search.root.right.value)
    expected = "bac"
    assert actual == expected

def test_binary_search_contains():
    search = BinarySearchTree()
    search.add("b")
    search.add("a")
    search.add("c")
    actual = search.contains("a")
    expected = True
    assert actual == expected