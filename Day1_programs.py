
#lambda function
#1
l=[1,2,3]
r=map(lambda x:x+x,l)
print(list(r))
res=map(lambda x:pow(x,2),l)
print(list(res))
s="jayanth"
(lambda s:print(s))(s)

#2
import math as m
l=[]
for i in range(0,15,2):
    l.append(i)
#r=map(lambda x:pow(x,1/2),l)
r=map(lambda x:m.sqrt(x),l)
print(list(r))

#abstraction
from abc import ABC,abstractmethod
class abstractdemo(ABC):
    @abstractmethod #called decorated to make the method abstract one
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
#changing abstract to concrete
class demo(abstractdemo):
    def display(self):
        print("abstraction method")
    def show(self):
        print("2nd function")
obj=demo()
obj.display()
obj.show()

#inheritance
#single level
#1
class parent:
    def display(self):
        print('parent class')
class child(parent):
    def show(self):
        print("child class")
c=child()
c.display()
c.show()
#2
class A:
    n=30
class B(A):
    def calc(self):
        c=self.n+30
        print(c)
obj=B()
obj.calc()
#multiple inheritance
class mom:
    def mdisplay(self):
        print("momclass")
class dad:
    def ddisplay(self):
        print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print("child class")
obj=child()
obj.mdisplay()
obj.ddisplay()
obj.cdisplay()
#multilevel inheritance
class grandparent:
    def display(self):
        print("grandparent class")
class parent(grandparent):
    def pdisplay(self):
        print("parent class")
class child(parent):
    def cdisplay(self):
        print('child class')
obj=child()
obj.cdisplay()
obj.display()
obj.pdisplay()''
#hierarchy inheritance
class parent:
    def mdisplay(self):
        print("momclass")
class child1(parent):
    def ddisplay(self):
        print("child1 class")
class child2(parent):
    def cdisplay(self):
        print("child2 class")
obj=child1()
obj.mdisplay()
obj.ddisplay() 
obj1=child2()
obj1.mdisplay()
obj1.cdisplay()
#hybrid inheritance
class parent:
    def mdisplay(self):
        print("momclass")
class child1(parent):
    def ddisplay(self):
        print("child1 class")
class child2(parent):
    def cdisplay(self):
        print("child2 class")
class kid1(child1):
    def k1display(self):
        print("kid1 class")
class kid2(child1):
    def k2display(self):
        print("kid2 class")
class kidd1(child2):
    def kd1display(self):
        print("kidd1 class")
class kidd2(child2):
    def kd2display(self):
        print("kidd2 class")
c1=kid1()
c1.k1display()
c1.ddisplay()
c1.mdisplay()
c2=kid2()
c2.k2display()
c2.ddisplay()
c2.mdisplay()
c3=kidd1()
c3.kd1display()
c3.cdisplay()
c3.mdisplay()
c4=kidd2()
c4.kd2display()
c4.cdisplay()
c4.mdisplay()
