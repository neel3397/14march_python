'''file handling:-we can create read and write in the using file handling in python programming

modes:

modes of file handling:

x-create file
r-read file
w-write file
a-append file'''

#f=open("test.txt","x")  #create file

#f=open("test.txt","r")
#print(f.read())

'''f=open("test.txt","w")
name=input("enter name:")
print(name)
f.write(name)

f.close()'''

'''f=open("test.txt","a")
name=input("enter name:")
print(name)
f.write(name)

f.close()'''

#read random line from python
#f=open("test.txt","r")
#print(f.readlines()[2])

'''n=int(input("how many lines you want to read?"))
f=open("test.txt","r")
for i in range(n):
    print(f.readline())'''

from shutil import copyfile
copyfile("test.txt","test1.txt")
