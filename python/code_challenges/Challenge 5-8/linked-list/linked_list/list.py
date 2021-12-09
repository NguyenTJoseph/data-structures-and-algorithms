class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    # Lab 06
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def toString(self):
        current = self.head
        string = ""
        while current:
            string += "{ " + current.value + " } -> "
            current = current.next

        string += "NULL"
        return string

    # Lab 07
    def append(self, value):
        current = self.head
        if current:
            while current.next != None:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)

    def insertBefore(self, target, newValue):
        current = self.head
        if current.value != target:
            while current.next.value != target:
                current = current.next
            nextNode = current.next

            current.next = Node(newValue, nextNode)

        else:
            self.head = Node(newValue, current)

    def insertAfter(self, target, newValue):
        current = self.head
        if current:
            while current.value != target:
                current = current.next
            current.next = Node(newValue, current.next)

        else:
            self.head = Node(newValue)

    # Lab 07
    def kthFromEnd(self, k):
        temp = []
        current = self.head
        while current and current.next != None:
            temp.append(current.value)
            current = current.next
        temp.append(current.value)

        try:
            return temp[len(temp) - k - 1]
        except IndexError:
            return Exception

    # Lab 08
    @staticmethod
    def linked_list_zip(list, list2):
        newList = LinkedList()
        start1 = list.head
        start2 = list2.head

        while start1.next != None and start2.next != None:
            newList.append(start1.value)
            newList.append(start2.value)
            start1 = start1.next
            start2 = start2.next
        newList.append(start1.value)
        newList.append(start2.value)

        if start1.next == None and start2.next != None:
            start2 = start2.next
            newList.append(start2.value)

        if start2.next == None and start1.next != None:
            start1 = start1.next
            newList.append(start1.value)

        return newList
