myset={"a","b","c","d","e"}
print(myset)

print(len(myset))

if "f" in myset:
    print("yes...")
else:
    print("no...")

for iteams in myset:
    print(iteams)    

myset.add("p")
print(myset)

myset.update("x","y","Z")
print(myset)

myset.remove("a")
print(myset)

myset.pop()
print(myset)

#del myset
#print(myset)


newset={"p","q","r","t"}
print(newset)
print(myset)

x=myset.union(newset)
print(x)

x=myset.intersection(newset)
print(x)
