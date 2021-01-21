class Node:
    def __init__(self,value=None):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,val):
        tempNode = Node(val)
        if self.head == None :
            self.head = tempNode
        else :
            temp = self.head
            while temp.next :
                temp = temp.next
            temp.next = tempNode

    def displayList(self):
        tempNode = self.head
        while tempNode is not None :
            print(tempNode.data,end='=>')
            tempNode = tempNode.next

if __name__ == "__main__":
    lst = LinkedList()
    for i in range(10):
        lst.insert(i)
    lst.displayList()