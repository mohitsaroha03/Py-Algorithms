#
import random 

class Stack:
    def __init__(self, C = 5):
        self.C = C
        self.array = []
    def size(self):
        return len(self.array)
    def isEmpty(self):
        return len(self.array) == 0
    def isFull(self):
        return len(self.array) == self.C
    def peek(self):
        if self.isEmpty():
            return None
        return self.array[self.size()-1]
    def pop(self):
        if self.isEmpty():
            print "Underflow"
            return None
        data = self.array.pop()
        return data
    def push(self, data):
        if self.isFull():
            print "Overflow"
            return
        self.array.append(data)

class AdvStack:
    def __init__(self):
        self.dataStack = Stack()
        self.minStack = Stack()
        self.minElement = 100000
    def push(self, data):
        self.dataStack.push(data)
        if data < self.minElement:
            self.minElement = data
        self.minStack.push(self.minElement)
    def pop(self):
        self.minStack.pop()
        data = self.dataStack.pop()
        return data
    def minimum(self):
        return self.minStack.peek()

testS = AdvStack()
testS.push(2)
print  testS.minimum()
testS.push(1)
print  testS.minimum()
testS.push(6)
print  testS.minimum()
testS.pop()
print  testS.minimum()
testS.pop()
print  testS.minimum()
