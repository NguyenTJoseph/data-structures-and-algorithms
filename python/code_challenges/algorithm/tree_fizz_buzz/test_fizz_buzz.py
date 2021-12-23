from tree_fizz_buzz import kArTree, Node, fizzBuzz

def test_fizz_buzz():
    tree = kArTree(3)
    a = Node(5)
    b = Node(3)
    c = Node(15)
    d = Node(5)
    e = Node(6)
    f = Node(7)
    g = Node(9)
    h = Node(6)
    a.children = [b,c,d]
    b.children = [e, f]
    c.children = [g]
    d.children = [h]
    tree.root = a
    newTree = fizzBuzz(tree)
    actual = (newTree.root.value + newTree.root.children[0].value + newTree.root.children[1].value + newTree.root.children[0].children[1].value)
    excepted = "BuzzFizzFizzbuzz7"
    assert actual == excepted
