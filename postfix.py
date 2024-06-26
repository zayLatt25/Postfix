class PostfixInterpreter:
    # Initialize the stack and the symbol table as empty lists
    def __init__(self):
        self.stack = []
        self.symbolTable = {}

    # Check if a token is a number by typecasting it to an integer
    def isNumber(self, token):
        try:
            int(token)
            return True
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
            try:
                operand2 = self.symbolTable[operand2]
            except KeyError:
                return "Variable not found: ", operand2

        # Pop the first operand from the stack
        operand1 = self.stack.pop(0)
        # Check if the operand is a variable
        # If it is a variable, get the value from the symbol table
        if self.isVariable(operand1):
            try:
                operand1 = self.symbolTable[operand1]
            except KeyError:
                return "Variable not found: ", operand1

        # Calculate the result and insert it into the stack
        result = eval(f"{operand1} {token} {operand2}")
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
        self.symbolTable[key] = value

        print("Symbol Table: ", self.symbolTable)

    # Evaluate the postfix expression
    def evaluate(self, expression):
        # Split the expression into tokens
        tokens = expression.split()

        # Iterate through the tokens
        for token in tokens:

            if self.isNumber(token):
                self.handleNumber(token)

            elif self.isVariable(token):
                self.handleVariable(token)

            elif self.isOperator(token):
                self.handleOperator(token)

            elif self.isAssignment(token):
                self.handleAssignment()

            # If the token is not a number, variable, operator, or assignment operator
            # Return an error message
            else:
                self.stack = []
                return f"Invalid token(s): {token} "

        # Return the top value of the stack if length is 1
        if len(self.stack) == 1:
            return self.stack.pop(0)

        # Clear the stack if the length of the stack is greater than 1
        if len(self.stack) > 1:
            self.stack = []

        # Otherwise return the stack []
        return self.stack


# Create an instance of the PostfixInterpreter class
interpreter = PostfixInterpreter()

print("")
print("-----Enter 'exit' to quit the program-----")

while True:

    # Get input from the user
    print("")
    expressionInput = input("Please enter your Postfix Expression: ")
    print("")

    # Check if the user wants to exit the program
    if expressionInput.lower() == "exit":
        break

    # Print the result of the evaluation of the expression
    print(interpreter.evaluate(expressionInput))
