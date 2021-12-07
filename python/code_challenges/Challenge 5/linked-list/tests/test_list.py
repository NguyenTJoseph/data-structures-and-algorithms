from linked_list.list import Node, LinkedList


def test_instantiate_list():
    lst = LinkedList()
    assert lst.head is None

def test_create():
    node = Node("a")
    actual = node.value
    expected = "a"
    assert actual == expected

def test_next():
    a = Node("a")
    b = Node("b", a)
    actual = b.next
    expected = a
    assert actual == expected

def test_insert_multiple():
    list = LinkedList()
    list.insert("a")
    list.insert("b")
    assert list.head.value == "b"
    assert list.head.next.value == "a"


def test_includes_t():
    list = LinkedList()
    list.insert("a")
    list.insert("b")
    actual = list.includes("a")
    expected = True
    assert actual == expected


def test_includes_f():
    list = LinkedList()
    list.insert("a")
    list.insert("b")
    actual = list.includes("c")
    expected = False
    assert actual == expected


def test_to_string():
    list = LinkedList()
    list.insert("a")
    list.insert("b")
    list.insert("c")
    assert list.toString() == "{ c } -> { b } -> { a } -> NULL"
