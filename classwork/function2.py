#normal function with normal parameter

def sum(a,b):  #parameter
    ans=a+b
    print(ans)
sum(10,20)    #argument


#args fuction

def addition(*n):
    ans=0
    for i in n:
        ans+=i
        print(ans)

addition(1,4,7,8,9)



#kwrgs

def myfun(**kwrgs):
    for k,v in kwrgs.items():
        print(f"{k}={v}")

myfun(name="neel",subject="maths",city="jodhpur")