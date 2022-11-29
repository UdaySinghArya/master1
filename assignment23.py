#Program-1-use iter and next method to access all the elments of a given set using while loop
'''
l1=(11,22,33,44,55)    #This is called container
it=iter(l1)  #   it=iterator object
while(True):
    e=next(it)    #   next method point to the next element of the container object .
    print(e)    #   e= obtainiing next element

'''
#yield=return
#return--after execution terminates program
#yield --after execution it resumeor hold
#Program-2-Create a generator to produce the first n odd  natural number.
'''
def odd(n):
    a=1
    while(n):
        yield a
        a+=2
        n-=1
it=odd(10)
while(True):
    e=next(it)
    print(e)
'''
#Program-3-Create a generator to produce the first n even natural number.
'''
def even(n):
    a=2
    while(n):
        yield a
        a+=2
        n-=1
n=10
it=even(n)
while(True):
    e=next(it)
    print(e)
'''
#Program-4-to find the square of first n natural number
'''
def N(n):
    a=1
    b=2
    while(n>0):
        yield a
        a=b*b
        b=b+1
        n=n-1
n=100
x=N(n)
while(True):
    e=next(x)
    print(e)
'''
#Program-5-To find the first n term of fibonacci series.
'''
def fib(n):
    a=0
    b=1
    c=a+b
    while(n>0):
        yield c
        a=b
        b=c
        c=a+b
        n=n-1
n=10
y=fib(n)
while(True):
    print(next(y))
'''
#program-6-To produce first n prime number
'''
def prime(n):
    m=50
    while(n>0):
        for x in range(1,20):
          if(x>1):
            for y in range(2,x):
                if(x%y==0):
                    break
            else:
                yield x
            n=n-1
it=prime(10)
while(True):
    print(next(it))
'''
#program-7-create an enless iterator using generator method to produce terms of fibonacci series
'''
def fib(n):
    a=0
    b=1
    c=a+b
    while(n):
        yield c
        a=b
        b=c
        c=a+b
n=0
it=fib(n)
while(True):
    print(next(it))
'''

#program-7-create an enless iterator using generator method to produce terms of prime numbers
'''
def prime(n):
    m=10000
    while(n):
        for x in range(1,m):
          if(x>1):
            for y in range(2,x):
                if(x%y==0):
                    break
            else:
                yield x
n=10
it=prime(n)
while(True):
    print(next(it))
'''

#Program-8-