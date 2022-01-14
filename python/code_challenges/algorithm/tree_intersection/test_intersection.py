from tree_intersection import tree_intersection, Node

def test_inter1():
    a = Node(12, Node(20, Node(15)))  
    b = Node(12, Node(20, Node(15))) 
    actual = tree_intersection(a, b)
    expected = [12, 20, 15]
    assert actual == expected
    print("test passed")

def test_inter2():
    a = Node(2, Node(5, Node(12)), Node(1, Node(15)))  
    b = Node(4, Node(2, Node(3))) 
    actual = tree_intersection(a, b)
    expected = [2]
    assert actual == expected
    print("test passed")

def test_inter3():
    a = Node(2, Node(5, Node(12)), Node(1, Node(15)))  
    b = Node(4, Node(21, Node(7)), Node(10, Node(27))) 
    actual = tree_intersection(a, b)
    expected = []
    assert actual == expected
    print("test passed")

test_inter1()
test_inter2()
test_inter3()