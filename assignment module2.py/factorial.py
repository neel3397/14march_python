n=int(input("enter a number:"))
factorial=1
if n==0:
    print("the factorial of [0] is [1]")

elif n<0:
    print("there cannot be factorial of negative number")

else:
    for i in range(1,n+1):
        factorial=factorial+1
        print(f"the factorial of [{n}] is [{factorial}]")