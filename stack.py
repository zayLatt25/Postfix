class Stack:
    # Initialize the stack using an array
    def __init__(self):
        self.stack = []

    def push(self, token):
        self.stack.insert(0,token)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

