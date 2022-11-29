#Program-1-To print the following status.
#a-a file is read only
#b-a file is closed or not.
#c-file opening mode is used.
#d-name of the  file.
'''
f=open('data1','r')
a=f.read()
print(a)
f.close()
'''
#Program-2-To create a new file 'myfile.txt' and store user entered text.
'''
f=open('myfile.txt','w')
f.write("Entered the text")
f.close()
'''
#program-3-to read the above created file 'myfile.txt' and display content on the console.
'''
f=open('myfile.txt','r')
a=f.read()
print(a)
'''
#program-4-To store a list of city names in a file 'cities.txt'.
'''
l1=['saharanpur',' ', 'mujjafarnagar',' ','merrut',' ','shamli']
f=open('cities.txt','w')
for x in l1:
    f.write(x)
f.close()
'''
#Program-5-To append of city names in a file 'cities.txt'.
'''
l1=[' ','ghazibad',' ','noida',' ','bagpat',' ','bijnor']
f=open("cities.txt",'a')
for x in l1:
    f.write(x)
f.close()
'''
#program-6-to search whether a particular city is there in the file 'cities.txt' or not.
'''
f=open("cities.txt",'r')
a=f.read()
l1=a.split(' ')
for x in l1:
    if('saharanpur'==x):
        print("yes present in list")
        break 
else:
        print("no")
'''
#Program-7-To count the number of python keyword occuring in a python source file.
'''
count=0
f=open("cities.txt",'r')
a=f.read()
l1=a.split(' ')
for x in l1:
    count=count+1
print("Number of words in the list::",count)
'''



#Program-8-To create a copy of file.
'''
import shutil

shutil.copyfile('myfile.txt','data1')

f=open('data1','r')
a=f.read()
print(a)
f.close()
'''
#Program-9-To store book data in a file .Book data is in the form of a dictonary in which book name is the key 
# and price is its value.Use pickle to store the into a file(say bookfile).
'''
import pickle

book={'Maths':200,'English':100,'Hindi':400,'Computer':300}
with open('file.txt','wb') as f: # or f=open('file.txt','wb')
    pickle.dump(book,f)  # to store the data

'''
#Program-10-To Extract book data from a book file using pickle.Also print extracted book data.
'''
import pickle
pickle_off=open('file.txt','rb')
a=pickle.load(pickle_off)   # to show the data
print(a)
'''
