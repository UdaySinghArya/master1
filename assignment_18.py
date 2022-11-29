#program-1-TO create and print a dictonary which stores your information
'''
d1={1:'uday',2:"singh",3:'arya'}
print(d1)
'''
#Program-2-To access the items of dictonary by referring to its key name.
'''
d1={1:'uday',2:"singh",3:'arya',4:'ustaad',5:'jaat'}
for x in d1:
    print(x,"......",d1[x])
'''
#Program-3-To get a list of the values from the dictonary
'''
l1=[]
d1={1:'uday',2:"singh",3:'arya',4:'ustaad',5:'jaat'}
for x in d1:
    l1.append(x)
print(l1)
'''
#Program-4-To change the value of specific item by reffering to its keys name
'''
d1={1:'uday',2:"singh",3:'arya',4:'ustaad',5:'jaat'}
d1[1]='English'
print(d1)
'''
#Program-5-To print all key names in the dictonary one by one
'''
d1={1:'uday',2:"singh",3:'arya',4:'ustaad',5:'jaat'}
for x in d1:
    print(x)
'''
#program-6-To create a dictonary that contain three dictonary
#Program-7-To create three dictonary,then create one dictonary that will contain the 
#other three dictonary
'''
d1={1:'uday',2:"singh",3:'arya',4:'ustaad',5:'jaat'}
d2={6:"mca",7:"bsc"}
d3={8:"maths",9:"english"}
d1.update(d2)
d1.update(d3)
print(d1)
'''
#Program-8-To convert two list into dictonary in a way that item from list1 is the key
#and item from list2 is the value.
'''
l1=[11,22,33,44,55]
l2=['uday','singh','arya','sakshi','sonam']
i=0
d1={}
while(i<=4):
    d1[l1[i]]=l2[i]
    i=i+1
print(d1)
'''
#Program-9-Merge Two python Dictonary into one dictonary
'''
d1={1:'uday',2:"singh",3:'arya',4:'ustaad',5:'jaat'}
d2={6:"mca",7:"bsc"}
d1.update(d2)
print(d1)
'''
#Program-10-To get the key of lowest value from the dictonary
'''
d1={92:'C',66:'java',85:'Python'}
print(min(d1))
d2={'C':78,'java':66,'Python':85}
print(min(d2))
'''



