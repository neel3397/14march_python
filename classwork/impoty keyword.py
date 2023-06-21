import keyword
keyword_list=keyword.kwlist
#print(keyword_list)
name=input("enter name:")
if name in keyword_list:
    print("it is keyword")
else:
    print("it is not keyword")