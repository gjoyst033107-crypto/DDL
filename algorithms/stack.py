
class Stack:
    def __init__(self):
        self.items = []

    # Add an element
    def push(self, value):
        self.items.append(value)
        return self.items

    # Remove the top element
    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty"

        return self.items.pop()

    # View the top element
    def peek(self):
        if len(self.items) == 0:
            return "Stack is empty"

        return self.items[-1]

    # Display stack
    def display(self):
        return self.items


# Example usage
my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Stack:", my_stack.display())
print("Top element:", my_stack.peek())

my_stack.pop()
print("After pop:", my_stack.display())
