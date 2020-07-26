# Link: 
# IsDone: 0
class Stack:
    def __init__(self):
        self.items = []
         
    # method for pushing an item on a stack
    def push(self, item):
        self.items.append(item)
         
    # method for popping an item from a stack
    def pop(self):
        return self.items.pop()
     
    # method to check whether the stack is empty or not
    def isEmpty(self):
        return (self.items == [])
     
    # method to get the top of the stack
    def peek(self):
        return self.items[-1]
     
    def __str__(self):
        return str(self.items)
 
 
def isPalindrome(str):
    strStack = Stack()
    palindrome = False
     
    for char in str:
        strStack.push(char)
         
    for char in str:
        if char == strStack.pop():
            palindrome = True
        else:
            palindrome = False
             
    return palindrome
 
print isPalindrome("madam")
