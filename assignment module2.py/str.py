str1=input("enter a string:")
str2=input("enter a string:")

x=str1[0:2]

str1=str1.replace(str1[0:2], str2[2:])
str2=str2.replace(str1[0:2], str2[2:])

print(str1+' '+str2)