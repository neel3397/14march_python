a=[10,20,30,40,40,50,30]
dup_items=set()
unique_items=[]

for x in a:
    if x not in dup_items:
        unique_items.append(x)
        dup_items.add(x)
print(dup_items)
