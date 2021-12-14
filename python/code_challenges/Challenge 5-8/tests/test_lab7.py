from linked_list.list import Node, LinkedList

def test_from_end_0():
    list = LinkedList()
    list.append("a")
    list.append("b")
    list.append("c")
    list.append("d")
    expect = "d"
    actual = list.kthFromEnd(0)
    assert expect == actual

def test_from_end_2():
    list = LinkedList()
    list.append("a")
    list.append("b")
    list.append("c")
    list.append("d")
    expect = "b"
    actual = list.kthFromEnd(2)
    assert expect == actual

def test_from_end_neg():
    list = LinkedList()
    list.append("a")
    list.append("b")
    list.append("c")
    list.append("d")
    expect = Exception
    actual = list.kthFromEnd(-1)
    assert expect == actual

def test_from_end_size_one():
    list = LinkedList()
    list.append("a")
    expect = "a"
    actual = list.kthFromEnd(0)
    assert expect == actual

def test_from_end_same():
    list = LinkedList()
    list.append("a")
    list.append("b")
    list.append("c")
    list.append("d")
    expect = "a"
    actual = list.kthFromEnd(3)
    assert expect == actual

def test_from_end_greater():
    list = LinkedList()
    list.append("a")
    list.append("b")
    list.append("c")
    list.append("d")
    expect = Exception
    actual = list.kthFromEnd(10)
    assert expect == actual
