with open(r"myfile.txt",'r')as fp:
    lines=len(fp.readlines())
    print('total number of lines:',lines)