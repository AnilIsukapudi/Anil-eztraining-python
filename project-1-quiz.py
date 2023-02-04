q1="""who is the best captain in india?
a)rohit sharma
b)captain cool
c)virat kohli
d)kapil dev"""
q2="""what is your college name?
a)pragati
b)aditya
c)jntuk
d)kl"""
q3="""prabhas next movie?
a)radhey syam
b)mirchi
c)salar
d)baahubali"""
q4="""kgf director?
a)raju
b)prabhas
c)yash
d) prashant neel"""
q5="""who is present prime minister of india?
a)jagan
b)kcr
c)nehru
d)modi"""
questions={q1:'b',q2:'a',q3:'c',q4:'d',q5:'d'}
name=input('hi what is ur name?')
print('hello',name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do you want skipthis ques (yes/no)")
    if flag1=="yes":
        continue
    ans=input('enter ur answer')
    if ans==questions[i]:
        print('correct')
        score+=1
        print('score',score)
    else:
        print('wrong')
        score-=1
        print('score',score)
    flag2=input("do you want quit (yes/no)")
    if flag2=="yes":
        break
print('ur total score:',score)
        
