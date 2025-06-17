print("Hello")

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return "Index out of bounds"
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1

    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value, end=" -> ")
            temp_node = temp_node.next
        print("None")

    def search(self, index):
        if index < 0 or index >= self.length:
            return None
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        print(temp_node.value)

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        temp_node.value = value
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        removed = temp_node.next
        temp_node.next = removed.next
        if index == self.length - 1:
            self.tail = temp_node
        self.length -= 1
        return removed

    def pop_first(self):
        if self.length == 0:
            return None
        removed = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return removed

    def pop(self):
        if self.length == 0:
            return None
        temp_node = self.head
        pre_node = self.head
        while temp_node.next:
            pre_node = temp_node
            temp_node = temp_node.next
        self.tail = pre_node
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return temp_node

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0


# --- Testing ---
ll = LinkedList()

print("--Append--")
ll.append(3)
ll.append(4)
ll.append(5)
print("Head:", ll.head.value)
print("Tail:", ll.tail.value)

print("--Prepend--")
ll.prepend(2)
ll.prepend(0)
print("Head:", ll.head.value)
print("Tail:", ll.tail.value)

print("--Insert at index 1--")
ll.insert(1, 1)

print("--Traverse--")
ll.traverse()

print("--Search index 0--")
ll.search(0)

print("--Set value at index 2 to 99--")
ll.set_value(2, 99)
ll.traverse()

print("--Remove node at index 2--")
removed = ll.remove(2)
print("Removed:", removed.value)
ll.traverse()

print("--Pop First--")
ll.pop_first()
ll.traverse()

print("--Pop Last--")
ll.pop()
ll.traverse()

print("--Reverse--")
ll.reverse()
ll.traverse()

print("--Clear--")
ll.clear()
ll.traverse()
