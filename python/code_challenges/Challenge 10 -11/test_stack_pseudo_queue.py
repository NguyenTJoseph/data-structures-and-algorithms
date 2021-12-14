from stack_and_queue import PseudoQueue
import pytest

def test_enqueue():
    queue = PseudoQueue()
    queue.enqueue("a")
    actual = queue.stackA.top.value
    expected = "a"
    assert actual == expected

def test_enqueue_multiple():
    queue = PseudoQueue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    actual = queue.stackA.top.value
    expected = "a"
    assert actual == expected


def test_dequeue():
    queue = PseudoQueue()
    queue.enqueue("a")
    queue.enqueue("b")
    actual = queue.dequeue()
    expected = "a"
    assert actual == expected
