#normal check vowel

l1=['a','e','u','m','c']

vowel_list=['a','e','i','o','u']
l2=[]

def checkvowel():
    for c in l1:
        if c in vowel_list:
            l2.append(c)
checkvowel()
print(l2)


#check vowel using filter method

a=['a','i','b','e','x']
vowel_list=['a','e','i','o','u']

def myfun(seq):
    if seq in vowel_list:
        return True
    else:
        return False
    
filtered_data=filter(myfun,a)

for i in filtered_data:
    print(i)


list=[10,56,78,34,32,90,12,3]
out=[]

for num in list:
    if num%2==0:
        out.append(num)
print(out)


def findmultiples(x):
    for i in range(1,x+1):
        if i%3==0:
            print(i)
findmultiples(3)