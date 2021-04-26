class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def createLinkedList(self):
        temp = 'y'
        while temp == 'y':
            print("Enter the Element : ")
            tempVal = int(input())
            if self.head is None:
                self.head = node(tempVal)
            else:
                tempHead = self.head
                while tempHead.next is not None:
                    tempHead = tempHead.next
                tempHead.next = node(tempVal)
            print("Want to enter More element ? y/n")
            temp = input()

    def createLinkedListAlt(self, lst):
        for item in lst:
            if self.head is None:
                self.head = node(item)
            else:
                tempHead = self.head
                while tempHead.next is not None:
                    tempHead = tempHead.next
                tempHead.next = node(item)

    def printList(self):
        print("Linked List ", end=': ')
        tempHead = self.head
        while tempHead is not None:
            print(tempHead.value, end='->')
            tempHead = tempHead.next

    def getLength(self):
        count = 0
        tempHead = self.head
        while tempHead is not None:
            count += 1
            tempHead = tempHead.next
        return count

    def appendList(self,val):
        temphead = self.head
        while temphead is not None:
            temphead = temphead.next
        temphead = node(val)

def addTwoNumbers(lst1,lst2):
    resultlst = linkedList()
    tempHeadlst1,tempHeadlst2,resultHead = lst1.head,lst2.head,resultlst.head
    if lst1.getLength() == lst2.getLength():
        while tempHeadlst1 is not None:
            resultlst.appendList(tempHeadlst1.value + tempHeadlst2.value)
            # resultHead = resultHead.next
            tempHeadlst1 = tempHeadlst1.next
            tempHeadlst2 = tempHeadlst2.next
    resultlst.printList()
    return resultlst


if __name__ == '__main__':
    lst1 = linkedList()
    lst2 = linkedList()
    sum = linkedList()
    lst1.createLinkedListAlt([1, 2, 3, 4, ])
    lst2.createLinkedListAlt([1, 2, 3, 4, ])
    sum = addTwoNumbers(lst1,lst2)
    sum.printList()