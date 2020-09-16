# Link: 
# IsDone: 0
class Stack(object):
    def __init__(self, items=[]):
        self.stack = items

    def is_empty(self):
        return not self.stack

    def pop(self):
        return self.stack.pop()

    def push(self, data):
        self.stack.append(data)

    def __repr__(self):
        return "Stack {0}".format(self.stack)

def reverseStack(stack):
    def reverseStackRecursive(stack, newStack=Stack()):
        if not stack.is_empty():
            newStack.push(stack.pop())
            reverseStackRecursive(stack, newStack)
        return newStack
    return reverseStackRecursive(stack)
def reverseStackRecursive(stack, newStack=Stack()):
    if not stack.is_empty():
        newStack.push(stack.pop())
        reverseStackRecursive(stack, newStack)
    return newStack

s = Stack(range(10))
print s
# print reverseStack(s)
print reverseStackRecursive(s)


