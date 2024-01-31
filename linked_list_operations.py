class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Function to get the value of a node at a specific index
def get_node_value(head, index):
    current = head
    for i in range(1, index):
        current = current.next

    current = current.next
    return current.value

# Function to add a new node at a specific index
def add_node(head, value, index):
    new_node = Node(value)
    if head is None:
        return new_node
    else:
        current = head
        for i in range(1,index):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head
    
# Function to delete a node at a specific index
def delete_node(head, index):
    if index == 0:
        return head.next

    current = head
    for i in range(1, index):
        current = current.next

    current.next = current.next.next
    return head



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

head = add_node(head, 7, 2)
head = delete_node(head, 3)

current = head
while current:
    print(current.value, end=" ")
    current = current.next
