class Dequeue:
    def __init__(self,queue = []):
        self.queue = queue

    def front_enqueue(self,value):
        self.queue.insert(0,value)

    def end_enqueue(self,value):
        self.queue.append(value)

    def is_empty(self):
        if len(self.queue) != 0 :
            return False
        else:
            return True

    def front_dequeue(self):
        if self.is_empty():
            exit("Error: Queue is Empty\nCannot Perform the Selected Operation\nTerminating Program...")
        else:
            temp = self.queue[::-1].pop()
            self.queue = self.queue[1:]
            return temp

    def end_dequeue(self):
        if self.is_empty():
            exit("Error: Queue is Empty\nCannot Perform the Selected Operation\nTerminating Program...")
        else:
            temp = self.queue[-1]
            self.queue = self.queue[:-1]
            return temp

    def show_dequeue(self):
        print(self.queue)

if __name__ == '__main__':
    q = Dequeue([-10,8,2,1,2,6])

