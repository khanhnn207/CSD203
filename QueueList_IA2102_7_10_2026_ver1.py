class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
        
class QueueList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    # enqueue <=> addLast
    def enqueue(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    #dequeue <=> removeFirst
    def dequeue(self):
        if(self.isEmpty()):
            print('Queue is empty. No dequeue')
            return
        x = self.head.data
        self.head = self.head.next
        return x
    
    def front(self):
        if(self.isEmpty()):
            print('Queue is empty. No element at front.')
            return
        x = self.head.data
        return x
            
   
if __name__ == '__main__':
    
    qu = QueueList()
    
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)
    qu.enqueue(4)
    qu.enqueue(5)
    qu.enqueue(6)
    
    print('The elements of queue in order FIFO: ')
    temp = qu.head
    while(temp != None):
        x = qu.dequeue()
        print(x, end = ' ')
        temp = temp.next

            