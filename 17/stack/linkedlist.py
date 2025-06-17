class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # fix this


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        return self.LinkedList.head is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.LinkedList.head
        self.LinkedList.head = new_node

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            node_value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node_value  # fix: return value

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList = None


# Test
s = Stack()
print(s.isEmpty())  # Should print True
s.push(10)
s.push(20)
print(s.peek())     # Should print 20
print(s.pop())      # Should print 20
print(s.pop())      # Should print 10
print(s.pop())      # Should print "Stack is Empty"
