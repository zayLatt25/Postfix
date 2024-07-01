class Stack:
    # Initialize the stack using an array
    def __init__(self):
        self.stack = []

    def push(self, token):
        self.stack.insert(0,token)

    def pop(self):
        return self.stack.pop(0)

    def size(self):
        return len(self.stack)
    
    def peek(self):
        return self.stack[0]
    
    # This function is for debugging and displaying purposes
    # Stack object does not have a printStack function
    def returnStack(self):
        return self.stack