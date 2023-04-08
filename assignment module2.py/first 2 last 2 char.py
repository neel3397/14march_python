mystr=input("enter a string:")

if len(mystr)<=2:
    print("empty string")

else:
    newstr=mystr[:2]+mystr[-2:]
    print("newstring is:",newstr)
