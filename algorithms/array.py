
class Array:
    def __init__(self):
        self.data = []

    # Display all elements
    def display(self):
        return self.data

    # Insert an element
    def insert(self, value, index):
        if index < 0 or index > len(self.data):
            return "Invalid index"

        self.data.insert(index, value)
        return self.data

    # Delete an element
    def delete(self, index):
        if index < 0 or index >= len(self.data):
            return "Invalid index"

        self.data.pop(index)
        return self.data

    # Access an element
    def access(self, index):
        if index < 0 or index >= len(self.data):
            return "Invalid index"

        return self.data[index]

    # Update an element
    def update(self, index, value):
        if index < 0 or index >= len(self.data):
            return "Invalid index"

        self.data[index] = value
        return self.data


# Example usage
my_array = Array()

my_array.insert(10, 0)
my_array.insert(20, 1)
my_array.insert(30, 2)

print("Array:", my_array.display())
print("Access index 1:", my_array.access(1))

my_array.update(1, 25)
print("After updating:", my_array.display())

my_array.delete(0)
print("After deleting:", my_array.display())
