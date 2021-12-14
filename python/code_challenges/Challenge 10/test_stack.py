import pytest

from stack_and_queue import Stack, InvalidOperationError

def test_push_onto_empty():
    stack = Stack()
    stack.push("a")
    actual = stack.top.value
    expected = "a"
    assert actual == expected

def test_push():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    actual = stack.top.value
    expected = "c"
    assert actual == expected

def test_pop_one():
    stack = Stack()
    stack.push("a")
    actual = stack.pop()
    expected = "a"

    assert actual == expected

def test_pop():
    stack = Stack()

    stack.push("a")
    stack.push("b")
    stack.push("c")

    actual = stack.pop()
    expected = "c"
    assert actual == expected

    actual2 = stack.top.value
    expected2 = "b"
    assert actual2 == expected2

def test_pop_all():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    actual = stack.peek()
    expected = "b"
    assert actual == expected

def test_peek_empty():
    stack = Stack()
    with pytest.raises(InvalidOperationError) as e:
        stack.peek()

def test_is_empty():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_pop_empty():
    stack = Stack()
    with pytest.raises(InvalidOperationError) as e:
        stack.pop()


