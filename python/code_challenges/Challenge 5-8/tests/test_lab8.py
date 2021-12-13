from linked_list.list import Node, LinkedList

def test_zip():
    list = LinkedList()
    list2 = LinkedList()
    list.append("a")
    list.append("b")
    list.append("c")
    list2.append("a")
    list2.append("b")
    list2.append("c")
    newlist = list.linked_list_zip(list, list2)
    assert newlist.toString() == "{ a } -> { a } -> { b } -> { b } -> { c } -> { c } -> NULL"


def test_zip_one_long():
    list = LinkedList()
    list2 = LinkedList()
    list.append("a")
    list.append("b")
    list.append("c")
    list2.append("a")
    list2.append("b")
    newlist = list.linked_list_zip(list, list2)
    assert newlist.toString() == "{ a } -> { a } -> { b } -> { b } -> { c } -> NULL"

def test_zip_other_long():
    list = LinkedList()
    list2 = LinkedList()
    list.append("a")
    list.append("b")
    list2.append("a")
    list2.append("b")
    list2.append("c")
    newlist = list.linked_list_zip(list, list2)
    assert newlist.toString() == "{ a } -> { a } -> { b } -> { b } -> { c } -> NULL"
