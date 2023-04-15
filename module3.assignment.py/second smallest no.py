li=[]
n=int(input("enter the number of elements:"))
for i in range(n,n+1):
    element=int(input("enter the elements:"))
    li.append(element)
li.sort()
print("the sorted list",li)
print("the second smallest value of this list:",li[1])