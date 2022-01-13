class Node:
    def __init__(self, key, value, next = None):
        self.value = {key : value}
        self.next = next


class HashTable:
    def __init__(self) -> None:
        self.buckets = [None for _ in range(0, 1024)]

    def add(self, key, value):
        sum = 0
        for char in key:
            sum += ord(char)

        sum = sum * 599 
        index = sum % 1024

        if self.buckets[index]:
            current = self.buckets[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

        else:
            self.buckets[index] = Node(key, value)

    def get(self, key):
        sum = 0
        for char in key:
            sum += ord(char)

        sum = sum * 599 
        index = sum % 1024
        current = self.buckets[index] 
        while current != None and current.next != None and key not in current.value:
            current = current.next
        if current != None and key in current.value:
            return current.value[key]



    def contains(self, key):
        sum = 0
        for char in key:
            sum += ord(char)

        sum = sum * 599 
        index = sum % 1024
        return self.buckets[index] != None


    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)

        sum = sum * 599 
        index = sum % 1024

        return index