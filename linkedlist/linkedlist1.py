class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value,end='->')
            temp=temp.next
    
    def insertEnd(self,val):
        tempNode=Node(val)
        if self.head==None:
            self.head=tempNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=tempNode
    
    def insertBeg(self,val):
        tempNode=Node(val)
        tempNode.next= self.head
        self.head=tempNode


    def insert(self,pos,val):
        temp=self.head
        while pos-1:
            temp=temp.next
            pos=pos-1
        tempNode=Node(val)
        tempNode.next=temp.next
        temp.next=tempNode

    def delete(self,val):
        temp=self.head
        if temp==None:
            print("Null List")
        elif val==self.head.value:
            self.head=self.head.next
        else:
            while temp.next :
                if temp.value == val:
                    break
                prev=temp
                temp=temp.next
            prev.next=temp.next
            print("item removed Successfully")

if __name__ == "__main__":
    datalist=linkedList()
    datalist.insertEnd("Monday")
    datalist.insertEnd("Tuesday")
    datalist.insertEnd("Wednesday")
    datalist.insertBeg("Sunday")
    datalist.insertEnd("Friday")
    datalist.insert(4,"Thursday")
    datalist.insertEnd("Saturday")
    datalist.delete("Sunday")
    datalist.printlist()

