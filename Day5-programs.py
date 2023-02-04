import random as r
x='hello world'
print(r.sample(x,2))

a=[1,2,3,4,5,6]
r.shuffle(a)
print(a)

a=[1,2,3,4,5,6]
print(r.choice(a))

b='welcome to python'
print(r.choice(b))

a=r.random()
print(a) #will return random number between 0.0 and 1.0
print(r.randint(20,30))

a=[10,20,30,40,50]
print(r.choices(a,k=10))

s='hello hi'
print(r.choices(s,k=3))

print(r.uniform(5,10))
A=dir(r)
print(A)


#calendar
import calendar
print('full calendar')
print(calendar.calendar(2023))

print('calendarof particular month')
print(calendar.month(2023,2))

print('set first day of the week')
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2023,3))


#datetime
import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y")
fv=a.strftime("%y")
print('year short version',sv)
print('year full version',fv)
z=dir(datetime)

#functions
def sample():
    print('this is python')
print('hello')
sample()
for i in range(4):
    sample()
    
#without argument without return value
def multi():
    n1=int(input("enter number"))
    n2=int(input("enter number"))
    n3=int(input("enter number"))
    print(n1*n2*n3)
multi()

#without argument with return value
def multi():
    n1=int(input("enter number"))
    n2=int(input("enter number"))
    n3=int(input("enter number"))
    return(n1*n2*n3)
res=multi()
print(res)

#with argument and without return value
def multi(n1,n2,n3):
    print(n1*n2*n3)
multi(4,5,6)
#user input
def multi1(a,b,c):
    print(a*b*c)
n1=int(input("enter number"))
n2=int(input("enter number"))
n3=int(input("enter number"))
multi1(n1,n2,n3)

#with argument and with return value
def multi(n1,n2,n3):
    return(n1*n2*n3)
res=multi(4,5,6)
print(res)
#user input
def multi1(a,b,c):
    return(a*b*c)
n1=int(input("enter number"))
n2=int(input("enter number"))
n3=int(input("enter number"))
res=multi1(n1,n2,n3)
print(res)

def lemons():
    x=int(input("enter no.of lemons u have:"))
    if x>21:
        print("excess lemons:",x-21)
    elif x<21:
        print("required lemons:",21-x)
    else:
        print('you have 21 lemons')
lemons()

#factorial
n=int(input('enter a number:'))
def fact():
    
    f=1
    for i in range(1,n+1):
        f*=i
    return f
result=fact()
print(result)

#multiplication table
n=int(input('enter a number:'))
def table(a,i):
    st=str(a)+"x"+str(i)+"="str(a*i)
    return st
for i in range(1,11):
    print(table(n,i))

#factors
n=int(input('enter a number:'))
def fact():
     for i in range(1,n+1):
         if n%i==0:
            print(i)
fact()

#sum of digits
def digits(n):
    sum=0
    while n!=0:
     rem=n%10   
     sum+=rem
     n=n//10
    return(sum)
n=int(input('enter a number:'))
res=digits(n)
print(res)
#recursive function
def display():
    n=int(input('enter a number:'))
    if n%2==0:
        display()
    else :
        print('over')
display()

#factorial using recursive function
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input('enter a number:'))
res=fact(n)
print(res)
    
 
