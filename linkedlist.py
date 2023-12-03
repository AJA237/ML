class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return self.value

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __self__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " <-> "
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
        
    def reverse_traversal(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.previous

    def pop(self):
        if not self.head:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = popped_node.previous
            self.tail.next = None
            popped_node.previous = None
        self.length -= 1
        return popped_node
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Index out of bounds.")
            return
        new_node = Node(value)
        if index == 0:
            self.pretend(value)
            return
        elif index == self.length:
            self.append(value)
            return
     def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node  = current_node.previous
        return current_node
    def set_value(self, index, value)