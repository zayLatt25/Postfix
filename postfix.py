from hashTable import HashTable

class PostfixInterpreter:
    # Initialize the stack and the symbol table as empty lists
    def __init__(self, hashTable):
        self.stack = []
        self.hashTable = hashTable

    # Check if a token is a number by typecasting it to an integer
    def isNumber(self, token):
        try:
            float(token)
            # Check if the number is greater than 0
            return True
        # If the token cannot be typecasted to an integer, it is not a number, return False
        except ValueError:
            return False

    # Insert the number into the stack
    def handleNumber(self, token):
        self.stack.insert(0, int(token))

    # Check if a token is a variable by checking if it is
    # not a number, operator, and an assignment operator
    def isVariable(self, token):
        return (
            not self.isNumber(token)
            and not self.isOperator(token)
            and not self.isAssignment(token)
            and token.isupper()
        )

    # Insert the variable into the stack
    def handleVariable(self, token):
        self.stack.insert(0, token)

    # Check if a token is an operator by checking if it is in the list of operators
    def isOperator(self, token):
        return token in ["+", "-", "*", "/"]

    # Handle the operator by popping two values from the stack,
    # applying the operator, and pushing the result back onto the stack
    def handleOperator(self, token):

        # Pop the second operands from the stack
        operand2 = self.stack.pop(0)
        # Check if the operand is a variable
        # If it is a variable, get the value from the symbol table
        if self.isVariable(operand2):
            # Save the variable name
            variable2 = operand2
            operand2 = hashTable.search(operand2)
            if operand2 is None:
                print("Variable not found:", variable2)
                return

        # Pop the first operand from the stack
        operand1 = self.stack.pop(0)
        # Check if the operand is a variable
        # If it is a variable, get the value from the symbol table
        if self.isVariable(operand1):
            # Save the variable name
            variable1 = operand1
            operand1 = hashTable.search(operand1)
            if operand1 is None:
                print("Variable not found:", variable1)
                return

        print(f"Operator Found! Calculating: {operand1} {token} {operand2}")
        # Calculate the result and insert it into the stack
        if token == "/":
            result = operand1 / operand2
        elif token == "*":
            result = operand1 * operand2
        elif token == "+":
            result = operand1 + operand2
        elif token == "-":
            result = operand1 - operand2

        # For display UI
        print(f"Result: {result}")
        print(f"Inserting {result} into the stack...")
        print(" ")
        self.stack.insert(0, result)

    # Check if a token is an assignment operator
    def isAssignment(self, token):
        return token == "="

    # Create and add the key-value pair to the symbol table
    def handleAssignment(self):
        # Pop the value from the stack
        value = self.stack.pop(0)
        # Check if the value is a variable
        if self.isVariable(value):
            print(f"Invalid assignment, {value} is in the place of number!")
            self.stack = []
            return

        # Pop the key from the stack
        key = self.stack.pop(0)
        # Check if the key is a number
        if self.isNumber(key):
            print(f"Invalid assignment, {key} is in the place of variable!")
            self.stack = []
            return

        # Add the key-value pair to the symbol table
        hashTable.insert(key, value)

        print("Symbol Table:", hashTable.table)

    # Check if a token is a delete operator
    def isDelete(self, token):
        if token == "!":
            return True
        return False
    
    # Delete the key-value pair from the symbol table
    def handleDelete(self):
        # Pop the key from the stack
        key = self.stack.pop(0)

        # Check if the key is a number
        if self.isNumber(key):
            print(f"Invalid delete, {key} is in the place of variable!")
            self.stack = []
            return

        # Delete the key-value pair from the symbol table
        hashTable.delete(key)

        print("Symbol Table:", hashTable.table)

    # Evaluate the postfix expression
    def evaluate(self, expression):
        # Split the expression into tokens
        tokens = expression.split()

        # Iterate through the tokens
        for token in tokens:

            print("Stack:", self.stack)
            print("Reading Token:", token)
            print("")

            if self.isNumber(token):
                self.handleNumber(token)

            elif self.isVariable(token):
                self.handleVariable(token)

            elif self.isOperator(token):
                # Perform an operation only if the stack has at least two values
                if len(self.stack) < 2:
                    print(
                        "Less than 2 elements left in the stack! Skipping remaining operations..."
                    )
                    break

                self.handleOperator(token)

            elif self.isAssignment(token):
                self.handleAssignment()

            elif self.isDelete(token):
                self.handleDelete()

            # If the token is not a number, variable, operator, or assignment operator
            # Return an error message
            else:
                self.stack = []
                print(f"Invalid Token Found: {token} ")
                return self.stack

        # Return the top value of the stack if length is 1
        if len(self.stack) == 1:
            # Check if the last value is a variable
            # Return empty stack if it is a variable
            if self.isVariable(self.stack[0]):
                self.stack = []
                return self.stack

            print("Expression Evaluated Successfully! Final Stack:", self.stack)
            print(" ")
            return self.stack.pop(0)

        # Clear the stack if the length of the stack is greater than 1
        if len(self.stack) > 1:
            self.stack = []
            print("Invalid Expression! Please check your expression and try again.")

        # Otherwise return the stack []
        return self.stack


# Create an instance of the HashTable class
hashTable = HashTable(26)

# Create an instance of the PostfixInterpreter class
interpreter = PostfixInterpreter(hashTable)

print("")
print("-----Enter 'exit' to quit the program-----")

while True:

    # Get input from the user
    print("")
    print("Enter 'variable !' to delete a variable from the symbol table")
    expressionInput = input("Please enter your Postfix Expression: ")
    print("")

    # Check if the user wants to exit the program
    if expressionInput.lower() == "exit":
        break

    # Print the result of the evaluation of the expression
    print(f"### Final Result: {interpreter.evaluate(expressionInput)} ###")
