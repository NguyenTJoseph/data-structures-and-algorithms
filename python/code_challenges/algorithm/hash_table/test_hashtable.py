from hash import HashTable

def test_hash1():
    table = HashTable()
    table.add("House", 23231)
    assert table.contains("House") == True
    
def test_hash2():
    table = HashTable()
    table.add("House", 23231)
    assert table.get("House") == 23231

def test_hash3():
    table = HashTable()
    table.add("House", 23231)
    assert table.hash("House") == 860

def test_hash4():
    table = HashTable()
    table.add("House", 2313)
    table.add("Hptse", 12121)
    assert table.hash("House") == table.hash("Hptse")
    assert table.get("House") == 2313
    assert table.get("Hptse") == 12121