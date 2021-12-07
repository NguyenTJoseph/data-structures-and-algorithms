from linked_list.list import Node, LinkedList

def test_append():
    list = LinkedList()
    list.insert("a")
    list.append("b")
    assert list.head.value == "a"
    assert list.head.next.value == "b"

def test_append_multiple():
    list = LinkedList()
    list.insert("a")
    list.append("b")
    list.append("c")
    assert list.head.value == "a"
    assert list.head.next.value == "b"
    assert list.head.next.next.value == "c"

def test_insert_before():
    list = LinkedList()
    list.insert("a")
    list.append("b")
    list.insertBefore("b", "c")
    assert list.toString() == "{ a } -> { c } -> { b } -> NULL"

def test_insert_before():
    list = LinkedList()
    list.insert("a")
    list.append("b")
    list.insertBefore("b", "c")
    assert list.toString() == "{ a } -> { c } -> { b } -> NULL"

def test_insert_before_first():
    list = LinkedList()
    list.insert("a")
    list.append("b")
    list.insertBefore("a", "c")
    assert list.toString() == "{ c } -> { a } -> { b } -> NULL"

def test_insert_after():
    list = LinkedList()
    list.insert("a")
    list.append("b")
    list.insertAfter("a", "c")
    assert list.toString() == "{ a } -> { c } -> { b } -> NULL"

def test_insert_after_last():
    list = LinkedList()
    list.insert("a")
    list.append("b")
    list.insertAfter("b", "c")
    assert list.toString() == "{ a } -> { b } -> { c } -> NULL"
