l=["neel","yash","richa"]
file1=open('myfile.txt','w')
file1.writelines()
file1.close()

file1=open('myfile.txt','r')
lines=file1.readlines()

count=0
for line in lines:
    count+=1
    print("line{}:{}".format(count,line.strip()))