#dictionary comprehension
d={n:n*n for n in range(1,5)}
print(d)

old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price) in old.items()}
print(new)

real={'sam':24,'angle':18,'kumar':35}
now={name:age for (name,age) in real.items() if age>20}
print(now)

#
import random
i=['jay','sri','hemanth','jayanth','sagar','sam','ravi','raj']
d={names:random.randint(1,100) for names in i}
print(d)

students=['jay','sri','hemanth','jayanth','sagar']
marks=[400,450,399,300,200]
d={name:(percnt/500)*100 for (name ,percnt) in zip(students,marks)}
print(d)

#strings
s='Python'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace('h','a'))
print(s.strip())
print(s.split('.'))
print(s.center(31,'*'))
print(s.count('y'))
print(s.count('o',1,len(s)))
print(s.endswith('o',0,len(s)))
print(s.find('t',0,len(s)))
print(s.index('y',0,len(s)))
print(s.islower())
print(s.isupper())
print(max(s))
print(min(s))
print(s.startswith('hello',0,len(s)))
print(s.rfind('h',0,len(s)))

#some string programs
s=input('enter a string:')
c=input('enter a character:')
if c in s:
    print('yes it is present')
else:
    print('no')

#
s=input('enter a string:')
p=0
for i in s:
    if i==' ':
        p+=1
if p!=0:
    print('no.of spaces',p )
else:
    print('no spaces')
#
s=input('enter a string:')
k=s[::-1]
if s==k:
    print('pallandrome')
else:
    print('not a palandrome')
#
s=input('enter a string:')
c=input('enter a character:')
a="yes" if c in s else no
print(a)

#
l=['a','e','i','o','u']
s=input('enter a string:')
count=0
for i in s:
    if i in l:
       count+=1
print(count)
    


