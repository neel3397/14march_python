stddata={"id":1,"name":"neel","sub":"python","id":1}#dictionary
print(stddata)#print the dictionary
#print(stddata["name"])  // to access the values
#print(stddata.get("sub")) //method to access the values of dictionary

#print(len(stddata))  //to find the length of dictionary

#print(stddata.keys()) // to print the key of dictionary
#print(stddata.values()) //to print the values of dictionary

if "neel" in stddata:
    print("yes...")
else:
    print("no...")

    if "neel" in stddata.values():
        print("yes...")
    else:
        print("no...")

for i in stddata.values():
    print(i)
for i in stddata.values():
    print(i)
for i in stddata.items():
    print(i)

for i,j in stddata.items():
    print(f"key={i} and value={j}")

stddata["city"]="ahmedabad"
print(stddata)

stddata.pop("sub")
print(stddata)

#stddata.clear()
#print(stddata)

#del stddata
#print(stddata)
newdict=stddata.copy()
print(newdict)