#To store all the programming language known to you using set
'''
b=set(input("Enter language you konw in the set \n").split(','))
print(b)
'''


#Program_2-To store your own information(name,age,gender,etc)
'''
b=set(input("Enter your detail::\n").split(','))
print(b)
'''


#Program_4-To find if"Python" is present in the set a={"java","Python","Django"}
#Program_5-Add items from the another set to the current set
'''
a={"java","python","sql"}
b={"c","c++","fortran"}
a.update(b)
print(a)
'''
#Program-6-To add elements of a list to a set
'''
a={"uday","singh","arya"}
b=["sakshi","sonam","arya"]
a.update(b)
print(a)
'''
#Program-7-To Remove last item of the given set
'''
a={"uday","singh","arya","ustaad"}
a.pop()
print(a)
'''
#Program-8-To delete the set completely
'''
a={"uday","singh","arya","ustaad"}
a.clear()
print(a)
'''
#program-9-Program To loop through the set and print values
'''
a={"python","Django","javascript","sql"}
for x in a:
    print(x)
'''
#program-10-To find the maximum and minimum value in the set 
'''
a={1,22,3,44,5,66,77}
b=min(a)
c=max(a)
print(b)
print(c)
'''
