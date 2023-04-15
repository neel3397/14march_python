def max_min(data):
    l=data[0]
    s=data[0]
    for num in data:
        if num>l:
            l=num
        elif num<s:
            s=num
    return l,s
print(max_min([4,6,9,1,5,68]))