#Program-1-To create a user class with 3 properties :name,age,email.
'''
class user:
    name="uday singh arya"
    age=21
    email="us85370@gmail.com"
n1=user()
print(n1.name)  # or user.name
print(n1.age)    # or user.age
print(n1.email)   # or user.email
'''
#Program-2-To create a user class with a method to greet the user.
'''
class user:
    def detail(self):
        self.name="uday singh arya"
        self.age=21
        self.email="us85370@gmail.com"

    
    
    def get_detail(self):
        print(self.name)
        print(self.age)
        print(self.email)
    
u1=user()
u1.detail()
u1.get_detail()
'''
#Program-3-To create 2 objects of the user class and assign different values.
'''
class user:
    def detail(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    

    def get_detail(self):
        print(self.name)
        print(self.age)
        print(self.email)

u1=user()
u2=user()
u1.detail("uday",21,"uday123")
u2.detail("aryan",20,"aryan123")

u1.get_detail()
u2.get_detail()
'''
#Program-4-To init default values for user object using __init__method.
'''
class user:
    def __init__(self):
        self.name="uday"
        self.age=21
        self.email="us85370@gmail.com"

u1=user()
print(u1.name)
print(u1.age)
print(u1.email)
'''

#Program-5-Wriye a program to delete the age property of the user.
'''
class user:
    def detail(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    
    def get_detail(self):
        print(self.name)
        print(self.age)
        print(self.email)
u1=user()
u1.detail("uday",21,"7uyyt")
del u1.age    # del keyword is used to delete any property
print(u1.name)
'''
#progranm-6-To find the greatest number between three object
'''
class user:
    def marks(self,m1):
        self.m1=m1
u1=user()
u1.marks(20)

u2=user()
u2.marks(3000)


u3=user()
u3.marks(100)

if(u1.m1>u2.m1  and u1.m1>u3.m1):
    print("grater number and object is ::",u1.m1,"u1")
elif(u2.m1>u3.m1):
    print("grater number and object is ::",u2.m1,"u2")
else:
    print("greater number and object is ::", u3.m1,"u3")
'''
#program-7-Write a python program to craete a laptop class with 4  
#attribute (brand,ram,cpu,hdd) and 2 methods(showconfig()) to 
# print the value,__init__() to initialize the values.
'''
class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def showconfig(self):
        print(self.brand)
        print(self.ram)
        print(self.cpu)
        print(self.hdd)

l1=laptop("DEL","8gb","processor","harddisk")
l1.showconfig()
'''
#Program-8-program to append the object in the list
'''
class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def showconfig(self):
        print(self.brand)
        print(self.ram)
        print(self.cpu)
        print(self.hdd)


list=[]
list.append(laptop("HP","4","processor1","harddisk1"))
list.append(laptop("DELL","16","processor2","harddisk2"))
list.append(laptop("LENVO","8","processor3","harddisk3"))

for l1 in list:
   print(l1.brand,l1.ram,l1.cpu,l1.hdd)
'''

#program-9-Write a python program to create 3 instance variable and 1
#class variable.
'''
class School:
    x=10
    def detail(self,name,address,student):
        self.name=name
        self.address=address
        self.student=student

s1=School()
s1.detail("RD NATIONAL","TALHERI",1000)
print(s1.x)
print(s1.name,s1.address,s1.student)
'''
#program-10-Program to get detail by the user
'''
class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    def getdetail(self):
        print(self.empid,self.name,self.salary)

e1=Employee(int(input("empid:")),str(input("name:")),int(input("salary:")))
e1.getdetail()
'''