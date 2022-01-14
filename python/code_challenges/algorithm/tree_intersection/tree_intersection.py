class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


from hashtable import HashTable 

def tree_intersection(head, otherhead):
    ht = HashTable()
    q = [head, otherhead]
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


