class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def printList(self):
        value = self.head
        while value is not None:
            print(value.val,end="->")
            value = value.next

if __name__ == '__main__':
    # e1 = Node(1)
    # e2 = Node(2)
    # e3 = Node(3)
    # e4 = Node(4)
    l = linkedList()
    l.head = Node(1)
    l.head.next = Node(2)
    l.head.next.next = Node(3)
    l.head.next.next.next = Node(4)
    l.printList()