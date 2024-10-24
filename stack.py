class Stack:

    def __init__(self, maximum=30):
        self.top = -1
        self.maximum = maximum - 1
        self.stack = []

    def lenght(self):
        return self.top + 1

    def push(self, item):
        if self.top >= self.maximum:
            print("Stack is full")
            return
        
        self.stack.append(item)
        self.top += 1

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
            return
        
        value = self.stack[self.top]
        self.top -= 1
        return value
    

    def isEmpty(self):
        if self.top == -1:
            return True
        
        return False
    
    def isFull(self):
        if self.top >= self.maximum:
            return True
        
        return False
    
    def peek(self):
        return self.stack[self.top]
    


stack = Stack(2)
stack.push(2)
print(stack.stack)
stack.push(3)
print(stack.stack)
stack.push(4)
stack.peek()
print(stack.stack)
stack.pop()
print(stack.stack)



