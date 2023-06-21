l=['no','country','for','old','men']
m=0
w=None
for i in range(len(l)):
    if len(l[i]>m):
        word=l[i]
        m=len(l[i])
print('longest word in the list is',word)