class BinarySearchTree:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def insertNode(self,newVal):
        if not self.value:
            self.value = newVal
            return
        if self.value == newVal:
            return
        if newVal < self.value:
            if self.left:
                self.left.insertNode(newVal)
                return
            self.left = BinarySearchTree(newVal)
            return
        if self.value > newVal:
            self.right.insertNode(newVal)
            return
        self.right = BinarySearchTree(newVal)


if __name__ == '__main__':
    root = BinarySearchTree(20)
    root.insertNode(10)
    root.insertNode(30)
    root.insertNode(15)
    root.insertNode(20)
    root.insertNode(35)
    root.insertNode(40)
    root.preorder(20)