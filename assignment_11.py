#program_1-sum of first n natural numbers
'''
sum=0
n=int(input("enter the value of n::"))
for x in range(1,n+1):
    sum=sum+x
print(sum)
'''
#program_2-sum of squares of first  n natural numbers
'''
sum=0
n=int(input("enter the value of n::"))
for x in range(1,n+1):
    y=x*x
    sum=sum+y
print(sum)
'''
#program_3-sum of first n odd natural numbers.
'''
sum=0
n=int(input("enter the value of n::"))
for x in range(1,n+1):
    if(x%2!=0):
        sum=sum+x
print(sum)
'''
#program-4-to find the factorial of a number
'''
fact=1
n=int(input("enter a number you want to find the factorial::"))
for x in range(n,0,-1):
    fact=fact*x
print(fact)
'''
#program_5-find the number of digits
'''
a=int(input("Enter a number"))
count=0
for x in str(a):
    count=count+int(True)
print(count))
'''
#program_6_find the sum of digits of number
'''
a=12311
sum=0
while(a>0):
    b=a%10
    sum=sum+b
    a=a//10
print(sum)
'''
