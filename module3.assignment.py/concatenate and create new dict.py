dic1={1:10,2:20}
dic2={4:40,5:50}
dic3={8:80,9:90}
dic4={}
for d in (dic1,dic2,dic3):dic4.update(d)
print(dic4)