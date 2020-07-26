# Link: 
# IsDone: 0
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self): 
        return self.items == []

    def addFront(self, item): # push
        self.items.append(item)

    def addRear(self, item): # pushing at index 0
        self.items.insert(0, item)

    def removeFront(self): # pop
        return self.items.pop()

    def removeRear(self): # poping at index 0
        return self.items.pop(0)

    def size(self):
        return len(self.items)
