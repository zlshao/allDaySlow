import pandas as pd
from builtins import str
txt1='0227Vote 8.txt'
txt2='0227Vote 16.txt'
txt3='0227Vote 32.txt'
txt4='0227Vote 64.txt'
str1='='
str2=';'
outfile='0227Vote all.txt'
def merge(fileList):
    L=[]
    ip = []
    for file in fileList:
        f = open(file, "r", encoding='utf-8')
        line = f.readline().splitlines()  # 读取第一行
        while line:
            L.extend(line)  # 列表增加
            line = f.readline().splitlines()  # 读取下一行
        # print(L)
        for s in L[1:]:
            loc1 = s.find(str1)
            loc2 = s.find(str2)
            temp = s[loc1 + 2:loc2 - 1]
            ip.append(temp)
    print(ip)
    ip=list(set(ip))
    ip.sort()

    f.close()


    f2 = open(outfile, 'w')
    length = len(ip)
    i=1
    f2.write('Ext_Count =' + str(length) + ';\n')
    for l in ip[1:]:
        print(l)
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f2.write(wt1)
        i += 1
    f2.close()
if __name__ == '__main__':
    filelist=[txt1,txt2,txt3]
    merge(filelist)
