#Program-1-To multiple 2 or 3 or 4 numbers with a single multiply method in a class using method overloading.
'''
class A:
    def __init__(self,a):
        self.a=a 


    def __mul__(self,other):  # operator overloading
        return self.a*other.a
    
a1=A(3)
a2=A(9)
a3=A(5)
a4=A(9)
x=a1*a2  # a1.__mul__(a2)
y=a3*a4   # a3.__mul__(a4)
print(x*y)
'''

#Program-2-To create user account class with 2 instance variables(userid and balance).Create 3 user objects 
# and add all the users using operator overloading.
'''
class user_account:
    def __init__(self,userid,balance):
        self.userid=userid
        self.balance=balance
    
    def __add__(self,other,x):  #OPERATOR OVERLOADING
        print(self.userid+other.userid+x.userid)
        print(self.balance+other.balance+x.balance)

a1=user_account(11,10)
a2=user_account(22,20)
a3=user_account(33,30)
a1.__add__(a2,a3)  # Add 3 objects
'''
#PROGRAM-3-To create a to print the above user account object using operator overloading(hint__str__method).
# In operator overloading rpr function is same as str function but the
#  priority of str function is more than rpr
'''
class user_account:
    def __init__(self,userid,balance):
        self.userid=userid
        self.balance=balance


    def __str__(self):
        print(self.userid,self.balance)
a1=user_account(11,22)
str(a1)
'''
#Program-4-To create two threads First thread will print all print all even  numbers and second
#  thread print will print all odd numbers till 100.

#In threading program function name should be 'run' by default
'''
from time import sleep
from threading import *

class A(Thread):
    def run(self):
        for x in range(1,101):
            if(x%2==0):
                print(x)
                
                sleep(1)
class B(Thread):
    def run(self):
        for x in range(1,101):
            if(x%2!=0):
                print(x)
                sleep(1)

a1=A()
b1=B()

a1.start()
b1.start()
'''
#Program-5-To create two threads to add all the values from 1 to 100.
'''
from time import sleep
from threading import *

class A(Thread):
    def run(self):
        sum=0
        for x in range(1,101):
            sum-sum+x
            print(sum)
            sleep(1)
class B(Thread):
    def run(self):
        sum=0
        for x in range(1,101):
            sum=sum+x
            print(sum)
            sleep(1)

a1=A()
b1=B()

a1.start()
b1.start()
'''
#Program-6-To create 5 threads to fill a list with random number till 100.
'''
from time import sleep
from threading import *

class A(Thread):
    def run(self):
        l1=[]
        for x in range(1,101):
            l1.append(x)
            print(l1)
            sleep(1)
        
class B(Thread):
    def run(self):
        l2=[]
        for x in range(1,101):
            l2.append(x)
            print(l2)
            sleep(1)
class C(Thread):
    def run(self):
        l3=[]
        for x in range(1,101):
            l3.append(x)
            print(l3)
            sleep(1)
class D(Thread):
    def run(self):
        l2=[]
        for x in range(1,101):
            l2.append(x)
            print(l2)
            sleep(1)
class E(Thread):
    def run(self):
        l2=[]
        for x in range(1,101):
            l2.append(x)
            print(l2)
            sleep(1)

a1=A()
b1=B()
c1=C()
d1=D()
e1=E()

a1.start()
b1.start()
c1.start()
d1.start()
e1.start()
'''
#Program-7-To create a clock where 1st thread will print the current time every
#  second and 2 thread will print "1 Minute completed" after every minute.
'''
from threading import *
from time import sleep
class A(Thread):
    def run(self):
        x=1
        while(True):
            if(x==60):
                x=1
            print(x)
            sleep(1)
            x=x+1
class B(Thread):
    def run(self):
        x=1
        while(True):
            sleep(59)
            print(x," minute completed")
            x=x+1

a1=A()
b1=B()
a1.start()
b1.start()
'''
#Program-8-Write a python script to change the name of the Thread.

#program-10-To check whether a given number is prime or armstrong number using different thread.
'''
from threading import *
class A(Thread):
    def run(self):
        a=7
        for b in range(2,a):
            if(a%b==0):
                print("Not prime")
                break
        else:
            print("prime")
class B(Thread):
    def run(self):
        sum=0
        c=153
        value=153
        while(c>0):
            d=c%10
            sum=sum+d*d*d
            c=c//10
        if(sum==value):
            print("armstrong number")
        else:
            print("Not armstrong number")
        

a1=A()
b1=B()
a1.start()
b1.start()
'''
#Program-9-Write a python script to join the 2 threads after printing completing the first question.
'''
from threading import Thread
from time import sleep
class A(Thread):
    def run(self):
        for x in range(0,5):
            print("hello\t")
            sleep(1)
class B(Thread):
    def run(self):
        for c in range(0,5):
            print("world")
            sleep(1)
a1=A()
b1=B()
a1.start()
b1.start()
'''