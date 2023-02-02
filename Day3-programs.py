#create the list with 10 elemnts and print one by one
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(i)
print('\n')
for j in range(len(l)):
    print(l[j])

#to calculate sum and average of list elements
l=[1.1,1.2,1.3,1.4,1.5]
for i in range(len(l)):
    i=sum(l)
print(i)
print('average:',i/len(l))

#even number in list
l=list(map(int,input('enter elements:').split()))[:6]
for i in l:
    if i%2==0:
        print(i)

size=int(input('enter:'))
l=[]
for i in range(size) :
    ele=int(input('elemets:'))
    l.append(ele)
print(l)
for j in l:
    if j%2==0:
        print(j)

#list comprehension
l=[i for i in 'Anil']
print(l)
l1=[2**j for j in range(1,9)]
print(l1)
l3=[1,2,3,4,5]
l4=[a for a in l3 if(a<5)]
print(l4)

#set
s={1,2,3,5.5}
s.add(10)
print(s)
s.update([3.6,5,4])
print(s)
s.discard(3.6)
print(s)
s1={1, 2, 3, 4}
s2={4, 5, 6, 7}
print(s1&s2)
print(s1^s2)
print(s1|s2)

#tuple
t=(4,3,4,9,6,"anil")
print(type(t))
print(t.count(4))
print(t.index(4))

#dictionary
d={1:"one",2:'two'}
print(d)
print(type(d))
print(d.keys())
print(d.values())
print(d.items())
print(d[1])
print(d.get(2))
print(d.pop(1))
print(d.items())
print(d.popitem())
print(d.items())



 
