class Student:
    def __init__(self,id,name,gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
        
    def showStudent(self):
        print(f'ID: {self.id},'
              f'Name: {self.name},'
              f'GPA: {self.gpa:.2f}')

class Node:
    def __init__(self,student):
        self.data = student
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def addLast(self,student):
        newNode = Node(student)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
    
    def addLastMany(self,a,b,c,n):
        for i in range(n):
            st = Student(a[i],b[i],c[i])
            newNode = Node(st)
            self.addLast(st)
    
    def addFirst(self,student):
        newNode = Node(student)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNoe
            return
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        
    def addAtIndex(self,student,index):
        if index <0 or index> self.size-1:
            print('The inputed index is invalid. No insertion!')
            return
        
        if index == 0:
            self.addFirst(student)
            return
        
        count = 0
        current = self.head
        while(count < index-1 and current != None):
            count += 1
            current = current.next
        newNode = Node(student)
        newNode.next = current.next
        current.next = newNode
        
        self.size += 1
        
    def removeFirst(self):
        if(self.isEmpty()):
            print('The list is empty. No deletion!')
            return 
        x = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        
        self.size -= 1
        return x
    
    def removeAtIndex(self,index):
        if(self.isEmpty()):
            print('The list is empty. No deletion!')
            return
        if index<0 or index >= self.size-1:
            print('The index is invalid. No deletion!')
            return
        if index == 0:
            x = ds.removeFirst()
            size -= 1
            return x
        
        count = 0
        current = self.head
        while(count <index-1 and current.next != None):
            count += 1
            current = current.next
        
        x = (current.next).data
        current.next = (current.next).next
        
        if(current.next == None):
             self.tail = current
             tail.next = None
        
        self.size -= 1      
        return x
    
    def removeLast(self):
        if self.isEmpty():
            print('The list is empty. No deletion!')
            return
        if self.head == self.tail:
            x = self.removeFirst()
            self.size -= 1
            return x
        
        current = self.head
        while(current.next != self.tail):
            current = current.next
        x = current.data
        self.last = current
        current.next = None
        
        self.size -= 1
        return x
        
            
    def display(self):
        current = self.head
        while (current != None):
            current.data.showStudent()
            current = current.next
   
if __name__ == '__main__':
    
    ds = LinkedList()
    a = [9,6,8,2,3]
    b = ['Nguyen Khoa Diem', 'Che Lan Vien', 'Vu Quan Phuong', 'Phan Thi Thanh Nhan', 'Cu Huy Can']
    c = [8.5, 9, 9.6, 7.8,8.0]
    print('===== 1. Test addLast and addLastMany =====')
    n = len(a)
    ds.addLastMany(a,b,c,n)
    ds.display()
    
    print('\n===== 2. Test addFirst =====')
    dd = int(input('Enter an id of new student: '))
    nn = input('Enter a name of new student: ')
    gg = float(input('Enter a gpa of new student: '))
    st = Student(dd,nn,gg)
    print('\nThe list after addFirst:')
    ds.addFirst(st)
    ds.display()
             
    print('\n===== 3. Test addAtIndex =====')
    dd = int(input('Enter an id of new student: '))
    nn = input('Enter a name of new student: ')
    gg = float(input('Enter a gpa of new student: '))
    st = Student(dd,nn,gg)
    idd = int(input('Enter a index where you want insert in to: '))
    print('\nThe list after addAtIndex:')
    ds.addAtIndex(st,idd)
    ds.display()
    
    print('\n===== 4. Test removeFirst =====')
    x = ds.removeFirst()
    x.showStudent()
    print(' was removed from the list')
    print('\nThe list after removedFirst:')
    ds.display()
    
    print('\n===== 5. Test removeAtIndex =====')
    ide = int(input('Enter a index where you want to remove student: '))
    y = ds.removeAtIndex(ide)
    y.showStudent()
    print(' was removed from the list')
    print('\nThe list after removedAtIndex:')
    ds.display()

    print('\n===== 6. Test removeLast =====')
    y = ds.removeLast()
    y.showStudent()
    print(' was removed from the list')
    print('\nThe list after removedLast:')
    ds.display()
            