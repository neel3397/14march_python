import operator
a={1:2,3:4,4:3,2:1}
print("original dictionary",a)
sd=sorted(a.items(), key=operator.itemgetter(1))
print('ascending order:',sd)
sd=dict(sorted(a.items(),key=operator.itemgetter(1)))
print('descending order:',sd)