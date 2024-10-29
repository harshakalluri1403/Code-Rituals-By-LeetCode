class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
# Create nodes
node1 = Node(1)
node2 = Node(6)
node3 = Node(3)

# Link nodes
node1.next = node2
node2.next = node3

# Create LinkedList and assign head
linked_list = LinkedList()
linked_list.head = node1

# Print the linked list
linked_list.print_linked_list()
