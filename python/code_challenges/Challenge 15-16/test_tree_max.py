from tree import BinarySearchTree

def test_binary_tree_max_1():
    search = BinarySearchTree()
    search.add(1)
    search.add(2)
    search.add(3)
    actual = search.findMax()
    expected = 3
    assert actual == expected

def test_binary_tree_max_2():
    search = BinarySearchTree()
    search.add(2)
    search.add(7)
    search.add(5)
    search.add(2)
    search.add(6)
    search.add(5)
    search.add(11)
    search.add(5)
    search.add(9)
    search.add(4)
    actual = search.findMax()
    expected = 11
    assert actual == expected