# Link: 
# IsDone: 0
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self): 
        return self.items == []

    def addFront(self, item): # push
        self.items.append(item)

    def addRear(self, item): # pushing from front
        self.items.insert(0, item)

    def removeFront(self): # pop
        return self.items.pop()

    def removeRear(self): # poping from front
        return self.items.pop(0)

    def size(self):
        return len(self.items)
