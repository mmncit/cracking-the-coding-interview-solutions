class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next

list = SLinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.head.next = e2

# Link second Node to third node
e2.next = e3

list.print()