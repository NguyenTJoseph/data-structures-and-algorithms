class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


from hashtable import HashTable 
def tree_intersection(head, morehead):
    ht = HashTable()
    q = [head, morehead]
    repeats = []
    while q:
        current = q.pop()
        if current.left:
            q.append(current.left)
        if current.right: 
            q.append(current.right)
        if ht.get(str(current.value)):
            iter = ht.get(str(current.value)) + 1
            
            ht.add(str(current.value), iter)
        else: 
            ht.add(str(current.value), 1)
    queue = [head]
    while queue:
        current = queue.pop()
        if current.left:
            queue.append(current.left)
        if current.right: 
            queue.append(current.right)
        if ht.get(str(current.value)) > 1:
            repeats.append(current.value)

    return repeats


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