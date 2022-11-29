#Program-1-To create a simple function Which print 'uday'
'''
def fun1(name):  #function defination
    print(name)

fun1('uday') #function call
'''
#Program-2-To aspect two argument and print them in the function body
'''
def fun1(a,b):
    print(a,b)
fun1('uday',2)
'''
#Program-4-To create a function which aspect kwargs(keywordargument) arguments.
'''
def fun1(a,b):
    print(a+b)
a=1
b=2
fun1(a,b) 
'''
#Program-5-To create a function which aspect a list as an argument
'''
l2=[]
def fun1(l2):
    print(l2)
l1=[11,22,33,44,55]
fun1(l1)
'''
#Program-6-To Use a function and find the maximum number between four numbers
'''
def fun1(a,b,c,d):
    x=a if a>d else d if a>c else c if a>b else b if b>d else d if b>c else c if c>d else d
    print(x)
a,b,c,d=int(input("1st=")),int(input("2nd=")),int(input("3rd=")),int(input("4th="))
fun1(a,b,c,d)
'''

#Program-7-BY Using Function To sum all the elements of list
'''
def fun1(l2):
    sum=0
    for x in l2:
        sum=sum+x
    print(sum)


l1=[11,22,33,44,55]
fun1(l1)
'''
#Program-7-BY Using Function To multiply all the elements of list
'''
def fun1(l2):
    mul=1
    for x in l2:
        mul=mul*x
    print(mul)
l1=[11,22,33,44,55]
fun1(l1)
'''
#Program-8-Check Whether a number is falls in range or not using function
'''
def fun1(x):
    r=range(1,10)
    for y in r:
        if(x==y):
            print("succesful")
            break
    else:
        print("unsuccesful")   
a=int(input("number::"))
fun1(a)
'''