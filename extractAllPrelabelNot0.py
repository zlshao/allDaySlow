import pandas as pd
from sklearn import tree
from sklearn .tree import DecisionTreeClassifier
file1='testsetLabeled 8.csv'
file2='testsetLabeled 16.csv'
file3='testsetLabeled 32.csv'
file4='testsetLabeled 64.csv'
outtxt='allPreNot0.txt'
def extract(file1,file2,file3,file4):
    IPlist=[]
    df = pd.read_csv(file1)
    dfPre = df.loc[(df['prelabel'] != 0)]
    IPlist.extend(dfPre['IP'].to_list())
    print(len(IPlist))

    df = pd.read_csv(file2)
    dfPre = df.loc[(df['prelabel'] != 0)]
    IPlist.extend(dfPre['IP'].to_list())
    print(len(IPlist))

    df = pd.read_csv(file3)
    dfPre = df.loc[(df['prelabel'] != 0)]
    IPlist.extend(dfPre['IP'].to_list())
    print(len(IPlist))

    df = pd.read_csv(file4)
    dfPre = df.loc[(df['prelabel'] != 0)]
    IPlist.extend(dfPre['IP'].to_list())

    IPlist=list(set(IPlist))


    print(len(IPlist))
    i = 1
    f = open(outtxt, 'w')
    length = len(IPlist)
    # f.write('TCP mixed =' + str(length) + ';\n')
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in IPlist:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1

if __name__=='__main__':
    extract(file1,file2,file3,file4)