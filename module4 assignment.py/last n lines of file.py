n=int(input("how many lines you want to read?"))
f=open("pc.txt","r")
for i in range(n):
    print(f.readlines())