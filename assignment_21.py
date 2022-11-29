
'''shortcut:::
1:print natural(n) ->> 1,2,3,4,...N
2:print natural(n-1) ->> 1,2,3,4...N-1
3:n==0
'''
#Program-1-Write a recrusive python function to print first N natural number
'''
def natural(n):
    if (n>0):
        natural(n-1)
        print(n)
n=10
natural(n)
'''
#Program-2-Write a recrusive python function to print first N natural number in reverse.
'''
def natural(n):
    if (n>0):
        print(n)
        natural(n-1)
n=10
natural(n)
'''
#Program-3-Using Recursive Function Find the odd numbers in reverse order 
'''
def odd(n):
    if(n>1):
        if(n%2==0):
            odd(n-1)
        else:
            print(n)
            odd(n-1)
    
m=int(input("enter number::"))        
odd(m)
'''
#Program-4-Using Recursive Function Find the odd numbers.
'''
def odd(n):
    if(n>1):
        if(n%2==0):
            odd(n-1)
        else:
            odd(n-1)
            print(n)
    
m=int(input("enter number::"))        
odd(m)
'''

#Program-5-Using Recursive Function Find first n the even numbers.
'''
def even(n):
    if(n>1):
        if(n%2==0):
            print(n)
            even(n-1)
        else:
            even(n-1)
    
m=int(input("enter number::"))        
even(m)
'''
#Program-6-Using Recursive Function Find first n the even numbers in reverse order.
'''
def even(n):
    if(n>1):
        if(n%2==0):
            even(n-1)
            print(n)
            
        else:
            even(n-1)
    
m=int(input("enter number::"))        
even(m)
'''
'''
#Program-7-To Print sqaure of first n natural number
def square(n):
    if(n>0):
        square(n-1)
        print(n*n)

m=int(input("natural number::"))
square(m)
'''

#Program-7-To Print cube of first n natural number
'''
def cube(n):
    if(n>0):
        cube(n-1)
        print(n*n*n)

m=int(input("natural number::"))
cube(m)
'''
#Program-9-To print fisrt n multiple of a given number
'''
def multiple(n,m):
    if(n>0):
        multiple(n-1,m)
        print(m*n)
        
b=int(input("Enter value which you generate table ::"))
a=int(input("end the table::"))
multiple(a,b)
'''
#Program-10-To print a number in revese order
'''
def reverse(n):
    if(n>0):
        print(n)
        reverse(n-1)
a=int(input("Enter a number you want reverse::"))
reverse(a)
'''