def happy(n):
    s=r=0
    while(n>0):
        for i in range(0,len(str(n))+1):
            r=n%10
            s+=r*r
            n=n//10
        return s
n= int(input('num'))
res=n
while(res!=1 and res!=4):
    res=happy(res)
if res==1:
    print('yes it is happy number')
else:
    print('unhappy number'
#protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print('encap fun-accessingb protected')
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)
#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print('encap fun-accessingb protected')
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj._a)

#polymorphism
#method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b) 
s=moverload()
s.display()
s.display(2,3)
s.display(5)
#overriding
class kkd:
    def placename(self):
        print('kkd')
    def student(self):
        print('yes-kkd')
    def year(self):
        print('3_year')
class hyd:
    def placename(self):
        print('hyd')
    def student(self):
        print('yes-hyd')
    def year(self):
        print('3_year')
c1=kkd()
c2=hyd()
for i in (c1,c2):
    i.placename()
    i.student()
    i.year()

#datastuctures
#linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next
obj=singlelinkedlist()
n=node("w")
obj.head=n
n1=node('I')
obj.head.next=n1
n2=node('N')
n1.next=n2
n3=node('N')
n2.next=n3
n4=node('E')
n3.next=n4
n5=node('R')
n4.next=n5
obj.display()
#insert a node at the beggining
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None    
    def insert_beggining(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
print('before inserting')
obj.display()
print('')
print('after insering')
obj.insert_beggining(100)
obj.display()
print('')
print('after insering')
obj.insert_beggining(200)
obj.display()
#inserting node at end of list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None    
    def insert_end(self,data):
        ne=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
obj.display()
print('after inserting')
obj.insert_end(100)
obj.display()
#insering a node at particular position
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None    
    def insert_position(self,pos,data):
        np=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
obj.display()
print('\nafter inserting')
obj.insert_position(2,1000)
obj.display()
#----------------------------------------
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=node(data)
            self.last_node=self.head
        else:
            self.last_node=self.next.last_node
    def display():
        current=self.head
        while current is not None:
            print(current.data,end='')
            current=current.next
a_llist=linkedlist()
n=int(input('how many'))
for i in range(n):
    data=int(input('enter data item:'))
    a_llist.append(data)
print('the linked list:',end='')
a_llist.display()
    
            
        
    
