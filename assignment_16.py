
#Program_1-To store Multiple items in a single variable(items "JAVA","PYTHON","C")
'''
a=input().split(",")
t=tuple(a)
print(t)
'''



#Program_2-To store one item using tuple
'''
a=("uday")
b=(1234)
print(type(a))
print(type(b))
'''


#Program_3-print Revrse the tuple
'''
a=(1,2,3,4)
b=a[::-1]
print(b)
'''


#Program_4-Swapping Of two Tuples
'''
a=(1,2,3,4)
print("!st tupe=",a)

b=(5,6,7,8)
print("2nd tupe",b)
c=()
c=a
a=b
b=c
print() 
print("After swapping\n")
print("!st tupe=",a)
print("!st tupe=",b)
'''


#Program_5-Remove duplicate value in the tuple
'''
a=(1,2,2,4,6,7,8,8,9,6,5,5)
b=tuple(set(a))
print(b)
'''

#'''Program_6-To divide the tuple'''
'''
a=(100,200,300,400)
for x in a:
    c=x//10
    print(c)
'''



#Program_7-To copy elements 4 and 5 from the following tuple into a new tuple.
'''
a=(1,2,3,4,5)
for x in a:
    b=a[3]
    c=a[4]
    break
c=(b,c)
print(c)
'''


#Program_8-To sort a Tuple of tuples by the second item


'''Program_9-To Print the vlues 20 from the nested tuple'''
'''
a=("Python",[10,20,30],(2,4,16))
b=a[1]
print(b[1])
'''


#Program_10-To change the first item(22) of a list with in the following tuple to 222
'''
a=(11,[22,33],44,55)

l1=list()
l1=list(a) #covert tuple into a list
#print(l1)

b=l1[1]
b[0]=222
#print(b)
#l1.insert(1,b)
print(tuple(l1))
'''










