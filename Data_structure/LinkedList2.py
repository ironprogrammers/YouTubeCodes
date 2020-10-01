class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

class DoublyLinkedListNode:

    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None

a1 = DoublyLinkedListNode(1)
b1 = DoublyLinkedListNode(2)
c1 = DoublyLinkedListNode(2)

a1.next_node = b1
b1.prev_node = a1
b1.next_node = c1
c1.prev_node = b1