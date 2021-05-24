class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        value = self.head
        while value is not None:
            print(value.val, end='')
            value = value.next
        print('\n')

    def insertBeg(self, newVal):
        node = Node(newVal)
        node.next = self.head
        self.head = node

    def insertEnd(self, newVal):
        node = Node(newVal)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node


if __name__ == "__main__":
    list1 = linkedList()
    list1.head = Node(1)
    ele2 = Node(3)
    ele1 = Node(2)
    list1.head.next = ele1
    ele1.next = ele2
    list1.printList()
    list1.insertBeg(0)
    list1.printList()
    list1.insertEnd(4)
    list1.printList()
