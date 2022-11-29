#Program_1-Get the character from the start to position 5
'''
s1="ineuron"
print(s1[0:5:1])
'''

#Program_2-Get the character from the 2 to position '
'''
s1="Hello Learners"
print(s1[1:5:1])
'''


#Program_3-To Demonstorate String conctenate adding space in between
'''
a="Learning"
b="Python"
print(a," ",b)
'''




#Program_4-To count Total number of Character in string a="ineuron"
'''
sum=0
count=1
a="ineuron"
for x in a:
    sum=sum+count
print("Total number of character=",sum)
'''



#Program_5-Reverse of string
'''
a="uday singh arya"
print(a[-1::-1])
'''



#Program_6-To determine whether a string contains a specific substring
'''
a="uday singh arya"
b="arya"
print(b in a)

'''

#program_7-Check if String Contain Only Numbers Using isdigit() method
'''
a=input("Enter value of a::")  #a should be string
if a.isdigit():
    print("a contain all numbers")
else:
    print("a not contain all numbers")
'''



#program_8-Check if String Contain Only alphabet Using isalpha() method
'''
a=input("Enter value of a::")  #a should be string
if a.isalpha():
    print("a contain all alphabet")
else:
    print("a not contain all alphabet")
'''
