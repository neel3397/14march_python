d1={'a':100,'b':200,'c':300}
d2={'b':300,'b':200,'c':400}

for key in d2:
    if key in d1:
        d2[key]=d2[key]+d1[key]

    else:
        pass
result=d1|d2
print(result)