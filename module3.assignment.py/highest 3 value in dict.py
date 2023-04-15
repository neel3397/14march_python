from heapq import nlargest
my_dict={'a':100,'b':1000,'c':200,'d':500,'e':900,'f':20}
three_largest=nlargest(3,my_dict,key=my_dict.get)
print(three_largest)