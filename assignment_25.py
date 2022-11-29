#program-1-To create profile class with 3 object attribuet(name,email,age)
#Program-2-To update the profile class with encapsulation

'''
class profile:
    def __init__(self):
        self.name="uday"
        self.email="us85370"
        self.age=21
    def set_profile(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
        

    def get_profile(self):
        return (self.name(),self.age(),self.email())    

p1=profile()
p1.set_profile("arya",22,"uadsteh73778")
print(p1.name,p1.age,p1.email)
'''

#Program-3-change email and age to __email and __age.
'''
class A:
    __email="us8474647"
    __age=22
class B(A):
    def change(self):
        b1.__email="udayarya87776"
        b1.__age=21
    def get_change(self):
        print(b1.__email,b1.__age)

a1=A()
b1=B()
b1.change()
b1.get_change()
'''
#Program-4-add a class variable(platform) and create a classmethod to access it.
'''
class employee:
    leaves=3
    
    @classmethod
    def change_leaves(cls,new_leaves):
        cls.leaves=new_leaves
    @classmethod
    def get_change(cls):
        print(cls.leaves)

e1=employee()
e1.change_leaves(5)
employee.leaves
employee.get_change()
'''
#program-5-create calculator class with 2 method for adding and subtracting 2 values.
'''
class calculator:
    def c1(self,a,b):
        return a+b

    def c2(self,c,d):
        return c-d



C1=calculator()
print(C1.c1(2,3))
print(C1.c2(10,3))
'''

#program-6-create class with 2 method for multiplication and division 2 values and inherit 
# it from the calculator class
'''
class calculator_2:
    def multiply(a,b):
        return a*b

class divide_1(calculator_2):
    def divide(self,c,d):
        if(c>=d):
            return c/d
        else:
            return d/c
    print(calculator_2.multiply(8,7))

C1=calculator_2()
d1=divide_1()
#print(d1.multiply(2,3))
print(d1.divide(2,10))
'''
#Program-7-To create a phone class with 2 method to print the features(calling and sms).
'''
class Phone:
    def fun1():  #Method 1
        print("FEATURES OF CALLING")
        print("call completion")
        print("call forwarding")
        print("call parking")
        print("call rejection")
        print("call screen")
        print("\n")

    def fun2(self):
        print("FEATURES OF SMS")
        print("It is versatile")
        print("It is real time")
        print("It is integrated")
        print("It is automated")
        print("It can be expanded")

p1=Phone()
Phone.fun1()  # access by class name
p1.fun2()   # access by reference object
'''
#Program-8-To create a SmartPhone class by inheritating calcucator_2 and Phone class
'''
class calculator_2:
    def multiply(a,b):
        print("\n",a*b)

class Phone(calculator_2):
    def fun1():  #Method 1
        print("FEATURES OF CALLING")
        print("call completion")
        print("call forwarding")
        print("call parking")
        print("call rejection")
        print("call screen")
        print("\n")

    def fun2():
        print("FEATURES OF SMS")
        print("It is versatile")
        print("It is real time")
        print("It is integrated")
        print("It is automated")
        print("It can be expanded")

class SmartPhone(Phone):
    Phone.fun1()
    Phone.fun2()
    calculator_2.multiply(2,9)
s1=SmartPhone()
'''

#program-9-To create a application like Truecaller where names and numbers are stored.
# Truecaller class will have 2 methods(1st to fetch the name and number and 2nd to add a new entry ).
"""
class Truecaller():
    def get_Details(self):
        print(self.name,self.number)

    def fetch(self,name,number):
        self.name=name
        self.number=number

t1=Truecaller()
t1.fetch(input("enter your name::"),int(input("Enter your number::")))
t1.get_Details()

"""

#Program-10-To add the new method in SmartPhone class Which accept Truecaller object
#  as a parameter and call the fetch method of Truecaller

class Truecaller():
    #def get_Details(self):
     #   print(self.name,self.number)

    def fetch(self,name,number):
        self.name=name
        self.number=number

        print(self.name,self.number)

class Phone():
    def fun1():  #Method 1
        print("FEATURES OF CALLING")
        print("call completion")
        print("call forwarding")
        print("call parking")
        print("call rejection")
        print("call screen")
        print("\n")

    def fun2():
        print("FEATURES OF SMS")
        print("It is versatile")
        print("It is real time")
        print("It is integrated")
        print("It is automated")
        print("It can be expanded")


class SmartPhone(Truecaller):
    Phone.fun1()
    Phone.fun2()
    def __init__(self,x):
        x.fetch(input("enter your name::"),int(input("Enter your number::")))
        #self.get_Details()
    
t1=Truecaller()
s1=SmartPhone(t1)

