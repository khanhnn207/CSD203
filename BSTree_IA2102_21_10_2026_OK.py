class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

class QNode:
    def __init__(self,p):
        self.info = p
        self.QNext = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isQEmpty(self):
        return self.head == None
    
    def enQueue(self,p):
        newNode = QNode(p)
        if self.isQEmpty():
            self.head = newNode
            self.tail = newNode
            return
        self.tail.QNext = newNode
        self.tail = newNode
        
    def deQueue(self):
        if self.isQEmpty():
            return None
        p = self.head.info
        self.head = self.head.QNext
        if self.head == None:
            self.tail = None
        return p
    
            
class BSTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def insert(self,x):
        newNode = Node(x)
        if(self.isEmpty()):
            self.root = newNode
            return
        
        current = self.root
        while True:
            if x == current.data:
                print(f'{x} exists in the tree. No insetion!')
                return
            if x<current.data:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            if x>current.data:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
                
    def insertMany(self,a,n):
        for i in range(n):
           self.insert(a[i])
           
    def deleteByMerging(self,x):
        if(self.isEmpty()):
            print('The tre is empty. No thing to delete')
            return
        #find out node with data x (node will be deleted)
        f = None
        p = self.root
        while p != None:
            if x == p.data:
                break
            f = p
            if x < p.data:
                p = p.left
            else:
                p = p.right
        if(p == None):
            print(f'{x} is not found. No thing to delete!')
            return
        #case 1: The node has no child
        if p.left == None and p.right == None:
            if p == self.root:
                self.root = None
                return
            if p == self.root.left:
                self.root.left = None
                return
            if p == self.root.right:
                self.root.right = None
                return
            if p == f.left:
                f.left = None
                return
            if p == f.right:
                f.right = None
                return
         #case 2: The node has only left child
        if p.left != None and p.right == None:
            if p == self.root:
                 self.root = self.root.left
                 return
            if p ==self.root.left:
                self.root.left = p.left
                return
            if p == self.root.right:
                self.root.right = p.left
                
            if p ==f.left:
                f.left = p.left
                return
            if p == f.right:
                f.right = p.left
                return
           
           #case 3: The node has only right child
            
        if p.left == None and p.right != None:
            if p == self.root:
                 self.root = self.root.right
                 return
            if p ==self.root.left:
                self.root.left = p.right
                return
            if p == self.root.right:
                self.root.right = p.right
                
            if p ==f.left:
                f.left = p.right
                return
            if p == f.right:
                f.right = p.right
                return   
                
         #case 4: The node has two children   
        if p.left != None and p.right != None:  
            # find out most right node of p'left subtree
            r = p.left
            while r.right != None:
                r = r.right
            # merging
            r.right = p.right
            p.right = None
            # delete p
            if p == self.root:
                self.root = self.root.left
                return
            if p == self.root.left:
                self.root.left = p.left
                return
            if p == f.left:
                f.left = p.left
                return
            if p == f.right:
                f.right = p.left
                return
            
    def deleteByCopying(self,x):
        if(self.isEmpty()):
            print('The tre is empty. No thing to delete')
            return
        #find out node with data x (node will be deleted)
        f = None
        p = self.root
        while p != None:
            if x == p.data:
                break
            f = p
            if x < p.data:
                p = p.left
            else:
                p = p.right
        if(p == None):
            print(f'{x} is not found. No thing to delete!')
            return
        #case 1: The node has no child
        if p.left == None and p.right == None:
            if p == self.root:
                self.root = None
                return
            if p == self.root.left:
                self.root.left = None
                return
            if p == self.root.right:
                self.root.right = None
                return
            if p == f.left:
                f.left = None
                return
            if p == f.right:
                f.right = None
                return
         #case 2: The node has only left child
        if p.left != None and p.right == None:
            if p == self.root:
                 self.root = self.root.left
                 return
            if p ==self.root.left:
                self.root.left = p.left
                return
            if p == self.root.right:
                self.root.right = p.left
                
            if p ==f.left:
                f.left = p.left
                return
            if p == f.right:
                f.right = p.left
                return
           
        #case 3: The node has only right child
            
        if p.left == None and p.right != None:
            if p == self.root:
                 self.root = self.root.right
                 return
            if p ==self.root.left:
                self.root.left = p.right
                return
            if p == self.root.right:
                self.root.right = p.right
                
            if p ==f.left:
                f.left = p.right
                return
            if p == f.right:
                f.right = p.right
                return   
                
        #case 4: The node has two children   
        if p.left != None and p.right != None:  
            # find out most right node of p'left subtree
            fr = p
            r = p.left
            while r.right != None:
                fr = r
                r = r.right
            
            # Copying
            p.data = r.data
            # delete r
            if r == self.root.left:
                self.root.left = r.left
                return
            if r == p.left:
                fr.left = r.left
                return
            
            if r == fr.left:
                fr.left = r.left
                return
            
            fr.right = r.left 
            
    #end deleteByCopying       
             
    def visit(self,p):
        if not p == None:
            print(p.data, end = ' ')
        
    def inOrder(self, p):
        if not p == None:
            self.inOrder(p.left)
            self.visit(p)
            self.inOrder(p.right)
    def preOrder(self, p):
        if not p == None:
            self.visit(p)
            self.preOrder(p.left)
            self.preOrder(p.right)
            
    def posOrder(self, p):
        if not p == None:
            self.posOrder(p.left)
            self.visit(p)
            self.posOrder(p.right)
            
    def breadthTraversal(self,p):
        if p == None:
            return
        k = Queue()
        k.enQueue(p)
        while not k.isQEmpty():
            temp = k.deQueue()
            self.visit(temp)
            if(temp.left != None):
                k.enQueue(temp.left)
            if(temp.right != None):
                k.enQueue(temp.right)
            
            
            
if __name__ == '__main__':
    t = BSTree()
    a = [7,4,9,8,5,2,1,6,3]
    n = len(a)
    t.insertMany(a,n)
    print('The tree inOrder is:') 
    t.inOrder(t.root)
    print('\nThe tree preOrder is:') 
    t.preOrder(t.root)
    print('\nThe tree posOrder is:') 
    t.posOrder(t.root)
    print('\nThe tree breadth first traversal is:') 
    t.breadthTraversal(t.root)
    print('\n\nThe tree after deletion a node: ')
    #t.deleteByMerging(3)
    t.deleteByCopying(3)
    t.inOrder(t.root)