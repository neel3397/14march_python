mydict={}

n=int(input("enter the number of pairs:"))

for i in range(n):
    key=input("enter the key:")
    value=input("enter the value:")
    mydict[key]=value
print(mydict)

