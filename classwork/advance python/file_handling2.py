#f=open("neel.txt","x")
f=open("neel.txt","a")

id=int(input("enter student id:"))
name=input("enter student name:")
subject=input("enter student subject:")


f.write(f"id:{id}")
f.write(f"name:{name}")
f.write(f"subject:{subject}")

f.close()
