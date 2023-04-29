items=["ball","bat","pitch","kit"]
file=open("iteams.txt","w")
for item in items:
    file.write(item+"\n")
file.close()