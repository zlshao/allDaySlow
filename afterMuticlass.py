#根据prelabel标记score 并提取扫描IP
import pandas as pd
from sklearn import tree
from sklearn .tree import DecisionTreeClassifier

# filename='bit16 0603/testsetLabeled0603 8 bit16.csv'
# outfile='bit16 0603/scoreNot0 8.csv'
# scanfile='bit16 0603/0603 8 bit16.txt'

filename='testsetLabeled 8.csv'
outfile='scoreNot0 8.csv'
scanfile='0227Vote 8.txt'

def writeScore(filename):
    df = pd.read_csv(filename)
    # dfPre = df.loc[(df['prelabel'] != 0)]

    dfsus1=df.loc[(df['prelabel'] ==1)]
    IPsus1=dfsus1['IP'].to_list()
    IPsus1=list(set(IPsus1))
    df1=df.loc[df['IP'].isin(IPsus1)]
    df1['score']=0
    for lip in IPsus1:
        dft = df1.loc[(df1['IP'] == lip)]
        length = dft.shape[0]  # lip的行数
        sum = dft['prelabel'].sum()  # 当前IP prelabel为1的行数
        if float(sum / length) > 0.5:
            df1['score'].loc[df1['IP'] == lip] = 11
    # df1.to_csv("test.csv")

    dfsus1=df.loc[(df['prelabel'] ==2)]
    IPsus1=dfsus1['IP'].to_list()
    IPsus1=list(set(IPsus1))
    df2=df.loc[df['IP'].isin(IPsus1)]
    df2['score']=0
    # df2.to_csv('test.csv')
    for lip in IPsus1:
        dft = df2.loc[(df2['IP'] == lip)]
        length = dft.shape[0]  # lip的行数
        sum = dft['prelabel'].sum()/2  # 当前IP prelabel为1的行数
        if float(sum / length) > 0.5:
            df2['score'].loc[df2['IP'] == lip] = 22

    dfsus1 = df.loc[(df['prelabel'] == 3)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df3 = df.loc[df['IP'].isin(IPsus1)]
    df3['score'] = 0
    # df1.to_csv('test.csv')
    for lip in IPsus1:
        dft = df3.loc[(df3['IP'] == lip)]
        length = dft.shape[0]  # lip的行数
        sum = dft['prelabel'].sum() / 3  # 当前IP prelabel为1的行数
        if float(sum / length) > 0.5:
            df3['score'].loc[df3['IP'] == lip] = 33

    dfsus1 = df.loc[(df['prelabel'] == 4)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df4 = df.loc[df['IP'].isin(IPsus1)]
    df4['score'] = 0
    # df1.to_csv('test.csv')
    for lip in IPsus1:
        dft = df4.loc[(df4['IP'] == lip)]
        length = dft.shape[0]  # lip的行数
        sum = dft['prelabel'].sum() / 4  # 当前IP prelabel为1的行数
        if float(sum / length) > 0.4:
            df4['score'].loc[df4['IP'] == lip] = 44

    dfsus1 = df.loc[(df['prelabel'] == 5)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df5 = df.loc[df['IP'].isin(IPsus1)]
    df5['score'] = 0
    # df1.to_csv('test.csv')
    for lip in IPsus1:
        dft = df5.loc[(df5['IP'] == lip)]
        length = dft.shape[0]  # lip的行数
        sum = dft['prelabel'].sum() / 5  # 当前IP prelabel为1的行数
        if float(sum / length) >0.5:
            df5['score'].loc[df5['IP'] == lip] = 55

    dfsus1 = df.loc[(df['prelabel'] == 6)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df6 = df.loc[df['IP'].isin(IPsus1)]
    df6['score'] = 0
    # df1.to_csv('test.csv')
    for lip in IPsus1:
        dft = df6.loc[(df6['IP'] == lip)]
        length = dft.shape[0]  # lip的行数
        sum = dft['prelabel'].sum() / 6  # 当前IP prelabel为1的行数
        if float(sum / length) > 0.5:
            df6['score'].loc[df6['IP'] == lip] = 66

    dfAll=pd.concat([df1,df2,df3,df4,df5,df6])
    dfAll.to_csv(outfile)






def extractScan(file):
    print('extrct scanIP')
    df = pd.read_csv(file)
    # df1 = df.loc[(df['Label'] == 4) |(df['Label'] == 18 )|(df['Label'] == 2)|(df['Label'] == 15)|(df['Label'] == 32)]
    df1 = df.loc[(df['score'] != 0)]
    # df1 = df1.loc[(df['prelabel'] == 1) | (df['prelabel'] == 2) | (df['prelabel'] == 3)]
    # df1 = df.loc[(df['prelabel'] !=0)]
    list1 = df1['IP'].to_list()
    # print(list1)
    newList = list(set(list1))
    newList.sort()
    i = 1
    f = open(scanfile, 'w')
    length = len(newList)
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in newList:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1
    f.close()


if __name__=='__main__':
    writeScore(filename)
    extractScan(outfile)













