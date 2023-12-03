from datetime import datetime
import random as rn

PACKAGES = {"standard", "premium", 'vip'}

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
    def pop_first(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            self.head.previous = None
            popped_node.next = None
        self.length -= 1
        return popped_node

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
    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False


    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value = target:
                return index
            current_node = current_node.next
            index += 1
        return -1


    def remove(self, index):
        if index < 0 or index >= self.length:
            
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        popped_node = self.get(index)
        popped_node.previous.next = popped_node.next
        popped_node.next.previous = popped_node.previous
        popped_node.next = None
        popped_node.previous = None
        self.length -= 1
        return popped_node

class SubscriptionHandler:
    def __init__(self, subscription):
        self.package = subscription

    def
