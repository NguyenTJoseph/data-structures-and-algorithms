from stack_and_queue import AnimalShelter


def test_enqueue_animal_single():
    queue = AnimalShelter()
    queue.enqueue("Wiley", "dog")
    actual = queue.dogs.front.value.name
    expected = "Wiley"
    assert actual == expected

def test_enqueue_animal_multiple():
    queue = AnimalShelter()
    queue.enqueue("Jerry", "dog")
    queue.enqueue("Suzy", "cat")
    queue.enqueue("Wiley", "dog")
    actual = queue.dogs.front.value.name
    expected = "Jerry"
    assert actual == expected

def test_dequeue_animal_single():
    queue = AnimalShelter()
    queue.enqueue("Wiley", "dog")
    actual = queue.dequeue("dog")
    expected = "Wiley"
    assert actual == expected

def test_dequeue_animal_multiple():
    queue = AnimalShelter()
    queue.enqueue("Jerry", "dog")
    queue.enqueue("Suzy", "cat")
    queue.enqueue("Wiley", "dog")
    actual = queue.dequeue("cat")
    expected = "Suzy"
    assert actual == expected
