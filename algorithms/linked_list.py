
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the end
    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Insert a node at the beginning
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Delete a node
    def delete(self, value):
        if self.head is None:
            return "Linked list is empty"

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return

            current = current.next

        return "Value not found"

    # Search for a value
    def search(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True

            current = current.next

        return False

    # Display all nodes
    def display(self):
        values = []
        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next

        return values


# Example usage
my_list = LinkedList()

my_list.insert(10)
my_list.insert(20)
my_list.insert(30)

print("Linked List:", my_list.display())

my_list.insert_at_beginning(5)
print("After inserting at beginning:", my_list.display())

my_list.delete(20)
print("After deleting 20:", my_list.display())

print("Search for 30:", my_list.search(30))
