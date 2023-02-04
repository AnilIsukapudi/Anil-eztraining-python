#exception handling
a=10
b=0
try:
    print(a/b)
except:
    print('this is except block')
print('end of program')

a=10
try:
    b=int(input('enter number:'))
    print('resource open')
    print(a/b)
except ZeroDivisionError as e:
    print('please note ,number cant be divided by zero',e)
except ValueError as e:
    print('invalid input',e)
except Exception as e:
    print('other error',e)
finally:
    print('end of program')
x=int(input('enter number:'))
if x%2!=0:
    raise Exception('x should be even')
else:
    print('x is even')
#oops
#classand object
class computer:
    def config(self):
        print('yes')
lenova=computer()
lenova.config()
dell=computer()
dell.config()

class employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print('ID: %d \nName:%s'% (self.id,self.name))
emp1=employee("jhon",101)
emp2=employee("zaka",102)
emp1.display()
emp2.display()

class computer:
    a=10
    b=20
    print('class variable i9nside class ',a)
    def config(self):
        c=100
        print('yes')
        print(' instance access',self.b)
lenova=computer()
print(lenova.a+lenova.b)
lenova.config()
dell=computer()
dell.config()


