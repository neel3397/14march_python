def multiplylist(mylist):
    result=1
    for x in mylist:
        result=result*x
    return result
#driver code
list1=[1,5,6]
list2=[3,5,9]
print(multiplylist(list1))
print(multiplylist(list2))