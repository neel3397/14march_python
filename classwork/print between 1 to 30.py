def printvalues():
    l=list()
    for i in range(1,21):
        l.append(i**2)
    print(l[:5])
    print(l[:-5])
printvalues()