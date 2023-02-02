#flot or int
a=36.5
if isinstance(a,float):
    print('a is float')
else:
    print('a is integer')
'''result=a-int(a)
if result != 0:
    print("it is float")'''

#divisile by both 2 and 5
n=int(input())
if n%2==0 and n%5==0:
    print('yes , it is divisible by 2 and 5')
else:
    print('no ,it is not divisible')

#divisible by 11
n=int(input())
if n%11==0:
    print(' yes it is divisible by  11')
else:
    print('no,it is not divisible by 11')

#biggest number
n1,n2=map(int,input().split())
if n1>n2:
    print('n1 is biggest:',n1)
else:
    print('n2 is biggest:',n2)

#three biggest numbers
n1,n2,n3=map(int,input().split())
if n1>n2 and n1>n3:
    print('n1 is biggest:',n1)
elif n2>n1 and n2>n3:
    print('n2 is biggest:',n2)
elif n3>n1 and n3>n2:
    print('n3 is biggest:',n3)

#even_odd
num=int(input(''))
if num%2==0:
    if num>0:
        print('number is even-positive')
    else:
        print('number is even-negative')
else:
    if num>0:
        print('number is odd-positive')
    else:
        print('number is odd-negative')



num=int(input(''))
if num==500:
    print('yes it is:500')
else:
    print('no,it is not 500')


#temperature
t=int(input())
if t>45:
     print('hottest')
elif t>40 and t<45:
     print('hot')
elif t>25 and t<40:
     print('moderate')
elif t>10 and t<25:
     print('COLD')
elif t<10:
     print('chill')
else:
    print('u may not enter number')

#bitwise operators
n1,n2=int(input("enter n1:")),int(input("enter n2:"))
print("bitwise and:",n1&n2)
print("bitwise or:",n1|n2)
print("bitwise xor:",n1^n2)

#differnt types of prints
print('its','a','good','day',end='  ')
print('all','is','good',sep='####',end='  ' )
print('joy')


#while loop
i=1
while i<=10:
    print(i)
    i+=1
print('\n')
i=1
while i<=30:
    print(i)
    i+=2
print('\n')
i=2
while i<=20:
    print(i)
    i+=2

#for loop
'''for i in range(1,11):
    print(i)'''
'''for i in range(2,11,2):
    print(i)
print('\n')'''
for i in range(10,1,-1):
    print(i)

#number game
import random
n= random.randrange(1,50)
guess=int(input("enter the number:"))
while n!= guess:
    if guess < n:
        print('too low !')
        guess=int (input("enter the number:"))
    elif guess > n:
        print('too high!')
        guess=int(input("enter the number:"))
    else:
        break
print('thats true')



    

