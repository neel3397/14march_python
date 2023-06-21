def getdata(id,name,sub):  #parameters  #function no.2  #static
    print("std id:",id)
    print("std name:",name)
    print("std sub:",sub)

getdata(1,"neel","computer")  #arguments

#dynamic

'''stdid=int(input("enter id:"))
stdname=input("enter name:")
stdsub=input("enter sub:")
getdata(stdid,stdname,stdsub)'''


n=int(input("how many students you want to enter?:"))
for i in range(n):
    stdid=int(input("enter id:"))
    stdname=input("enter name:")
    stdsub=input("enter sub:")
    getdata(stdid,stdname,stdsub)
 
