from stack_and_queue import Queue, InvalidOperationError
import pytest

def test_enqueue():
    queue = Queue()
    queue.enqueue("a")
    actual = queue.front.value
    expected = "a"
    assert actual == expected

def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    actual = queue.front.next.next.value
    expected = "c"
    assert actual == expected

def test_dequeue():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    actual = queue.dequeue()
    expected = "a"
    assert actual == expected

def test_peek():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    actual = queue.peek()
    expected = "a"
    assert actual == expected

def test_dequeue_all():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.dequeue()
    queue.dequeue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_instantiate():
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_peek_empty():
    queue = Queue()
    with pytest.raises(InvalidOperationError):
        queue.peek()

def test_dequeue_empty():
    queue = Queue()
    with pytest.raises(InvalidOperationError):
        queue.dequeue()
