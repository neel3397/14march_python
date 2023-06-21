s1=int(input("enter the marks of subject1:"))
s2=int(input("enter the marks of subject2:"))
s3=int(input("enter the marks of subject3:"))
s4=int(input("enter the marks of subject4:"))

if s1>=35 or s2>=35 or s3>=35 or s4>=35:

    total=s1+s2+s3+s4
    print("total=",total)

    per=total/4
    print("percentage=",per)

    if per>=70:
        print("result:distinction")
    elif per>=60:
        print("result:first class")
    elif per>=50:
        print("result:second class")   

    elif per>=40:
        print("result:pass class") 


    else:
        print("fail")