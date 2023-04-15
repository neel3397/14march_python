list=[]
num=int(input("how many numbers:"))

for n in range(num):
    numbers=int(input("enter number"))

    list.append(numbers)
print("maximum element in list is",max(list),"\n minimum elment in the list is:",min(list))