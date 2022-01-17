from hash import HashTable
from join import left_join

def test_join1():
    a = HashTable()
    a.add("diligent", "employed")
    b = HashTable()
    b.add("diligent", "idle")
    actual = left_join(a, b)
    expected = [['diligent', 'employed', 'idle']]
    assert actual == expected
    
def test_join2():
    a = HashTable()
    a.add("diligent", "employed")
    b = HashTable()
    b.add("diligent", "idle")
    b.add("fond", "enamored")
    actual = left_join(a, b)
    expected = [['diligent', 'employed', 'idle'], ["fond", "enamored"]]
    assert actual == expected

def test_join3():
    a = HashTable()
    a.add("diligent", "employed")
    a.add("fond", "enamored")
    a.add("guide", "usher")
    a.add("outfit", "garb")
    a.add("wrath", "anger")
    b = HashTable()
    b.add("diligent", "idle")
    b.add("fond", "averse")
    b.add("guide", "follow")
    b.add("flow", "jam")
    b.add("wrath", "delight")
    actual = left_join(a, b)
    expected = [['diligent', 'employed', 'idle'], ['outfit', 'garb'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'], ['flow', 'jam']]
    assert actual == expected

