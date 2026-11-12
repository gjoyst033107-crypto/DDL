
class Queue:
    def __init__(self):
        self.items = []

    # Add an element
    def enqueue(self, value):
        self.items.append(value)
        return self.items

    # Remove the first element
    def dequeue(self):
        if len(self.items) == 0:
            return "Queue is empty"

        return self.items.pop(0)

    # View the first element
    def front(self):
        if len(self.items) == 0:
            return "Queue is empty"

        return self.items[0]

    # Display queue
    def display(self):
        return self.items


# Example usage
my_queue = Queue()

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print("Queue:", my_queue.display())
print("Front element:", my_queue.front())

my_queue.dequeue()
print("After dequeue:", my_queue.display())
