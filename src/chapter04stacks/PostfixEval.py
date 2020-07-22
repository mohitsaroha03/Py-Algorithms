''

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
     
    def __str__(self):
        return str(self.items)

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('1 2 3 * + 5 - '))
