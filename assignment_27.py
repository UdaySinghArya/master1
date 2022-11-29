#EXCEPTION HANDLING OVER VIEW
#  try:Run this code
#  except:Excute this code when there is an exception.
#  else: No Exception?Run this code.
#  finally: Always run this code.
   
#Program-1-To create an ArithmeticError
'''
a=10
b=0
c=a/b
print(c)
'''
#Program-2-To create an ValueError
'''
import math
a=int(input("Enter a positive number"))
b=math.sqrt(a)
print(b)
'''
#Program-3-To handle the ArithmeticError
'''
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=0
try:
    c=a/b
except ZeroDivisionError:
    print("Donot write zero")
else:
    print(c)
finally:
    print("program end")
'''
#Program-4-To handle ValueError
'''
import math
a=int(input("enter a number you want to find squareroot:"))
try:
    b=math.sqrt(a)
except ValueError:
    print("Enter valid number")
else:
    print(b)
finally:
    print("program end")
'''
#Program-5-To handle multiple exception in one try
'''
c=100
d=0
a='u'
b=6
try:
    e=c/d
    print("division is:",e)
    c=a+b
    print("sum is ",c)
except ZeroDivisionError:
    print("In division, we cannot divide by zero")
except TypeError:
    print("In addition Your typing mistake")
finally:
    print("program end")
'''
#Program-6-To create a calculator with 4 basic operation and handle a maximum number of exception
'''
choice=input("enter operation you want to perform:")
a=int(input("enter number::"))
b=int(input("enter number::"))

try:
    if(choice=="add"):
        c=a+b
        print("add is ",c) 

    elif(choice=="subtract"):
        c=a-b
        print("subtract is ",c) 

    elif(choice=="multiply"):
        c=a*b
        print("multiply is ",c) 
    
    elif(choice=="division"):
        if(a>b):
            c=a/b
            print("division is :",c)
        else:
            c=b/a
            print("division is :",c)

except ZeroDivisionError:
    print("you can not divide by zero of any number")
except Exception:
    print("Enter valid choice")
finally:
    print("calculator off")
'''
#Program-7-To add a finally block for the above script.
#Program-8-To implement try except and else block for division.
'''
a=int(input("enter a number::"))
b=int(input("enter a number::"))
try:
    c=a/b
        
        
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("division is ",c)
'''
#Program-9-To raise a ValueError.
'''
b='s'
try:
    a=int(input("Enter a number:"))
    #num=int(b)
    x=a+b
#except TypeError:
#    print("you cannot add one string and one integer")

except ValueError:
    raise ValueError("you cannot change string into int")

print("sum is ",x)
'''
#Program-10-To implemented a nested Try Excepted block.
'''
try:
    print("outer try")
    #print(10/0)
    try:
        print("inner try")
        print(10/0)
    except NameError:  # Extra
        print("This is called NameError")
    except ZeroDivisionError:
        print("inner except")
except:
    print("Outer except block")
'''













