#Program_4-print all prime number between two numbers.
'''
l=int(input("enter lower limit:"))
m=int(input("enter uper limit:"))
for n in range(l,m):
    if(n<1):
        print("invalid number")
    else:
        for x in range(2,n):
            if(n%x==0):
                break
        else:
                print(n)

'''
#program_5-print next prime number 
'''
n=int(input())
while True:
    n=n+1
    for x in range(2,n):
        if n%x==0:
            break
    else:
        print("next Prime No. is ",n)
        break
    
'''
'''
x=int(input("Enter colour "))
if(x==1 or x==2 or x==3 or x==4 or x==5 or x==6 or x==7):
    match x:
        case 1:
            print("Monday")
        
        case 2:
            print("Tuesday")

        case 3:
            print("Wednesday")

        case 4:
            print("Thrusday")

        case 5:
            print("Friday")

        case 6:
            print("Saturday")

        case 7:
            print("Monday")
'''