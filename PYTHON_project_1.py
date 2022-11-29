#PROJECT NAME--- "WORD PUZZLE GAME"

def fun(i):
    count=0
    n=''    
    total=0
    
    
    l1=[]
    w=['uday','pradeep','chaudhary','naveen','shaurabh']
    a=w[i]
    for x in a:
        l1.append(x)

    for x in range(0,len(l1)):
        r=random.randint(0,len(l1)-1)
        n=n+l1[r]
        l1.pop(r)
    print(n)
    l1.clear()
    ch1=input("Guess the name::")
    
    if(ch1==a):
        print("corret\n")
        count=count+1
        return count
    else:
        print("Incorret\n")
        total=total-1
        return total
        
import random
i=0
c=0
d=0
e=0
f=0
g=0

c=fun(i)
i=i+1
d=fun(i)
i=i+1
e=fun(i)
i=i+1
f=fun(i)
i=i+1
g=fun(i)

result=c+d+e+f+g
print("Net Score::",result)

