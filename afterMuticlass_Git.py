import pandas as pd
#----------------------------------------------输入文件和输出文件------------------------------------------
filename='testsetLabeled 64.csv'    #输入文件
outCsvFile='scoreNot0 64.csv'       #中间输出文件
outScannerIPFile='0519Vote 64.txt'  #输出扫描器IP地址

#-----------------------------------------根据报警比例进行筛选输出到中间文件----------------------------------
alarm_ratio=0.5
def writeScore(filename):
    df = pd.read_csv(filename)
    dfsus1=df.loc[(df['prelabel'] ==1)]
    IPsus1=dfsus1['IP'].to_list()
    IPsus1=list(set(IPsus1))
    df1=df.loc[df['IP'].isin(IPsus1)]
    df1['score']=0
    for lip in IPsus1:
        dft = df1.loc[(df1['IP'] == lip)]
        length = dft.shape[0]
        sum = dft['prelabel'].sum()
        if float(sum / length) > alarm_ratio:
            df1['score'].loc[df1['IP'] == lip] = 11

    dfsus1=df.loc[(df['prelabel'] ==2)]
    IPsus1=dfsus1['IP'].to_list()
    IPsus1=list(set(IPsus1))
    df2=df.loc[df['IP'].isin(IPsus1)]
    df2['score']=0
    for lip in IPsus1:
        dft = df2.loc[(df2['IP'] == lip)]
        length = dft.shape[0]
        sum = dft['prelabel'].sum()/2
        if float(sum / length) > alarm_ratio:
            df2['score'].loc[df2['IP'] == lip] = 22

    dfsus1 = df.loc[(df['prelabel'] == 3)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df3 = df.loc[df['IP'].isin(IPsus1)]
    df3['score'] = 0
    for lip in IPsus1:
        dft = df3.loc[(df3['IP'] == lip)]
        length = dft.shape[0]  # lip的行数
        sum = dft['prelabel'].sum() / 3
        if float(sum / length) > alarm_ratio:
            df3['score'].loc[df3['IP'] == lip] = 33

    dfsus1 = df.loc[(df['prelabel'] == 4)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df4 = df.loc[df['IP'].isin(IPsus1)]
    df4['score'] = 0
    for lip in IPsus1:
        dft = df4.loc[(df4['IP'] == lip)]
        length = dft.shape[0]
        sum = dft['prelabel'].sum() / 4
        if float(sum / length) > 0.4:
            df4['score'].loc[df4['IP'] == lip] = 44

    dfsus1 = df.loc[(df['prelabel'] == 5)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df5 = df.loc[df['IP'].isin(IPsus1)]
    df5['score'] = 0
    for lip in IPsus1:
        dft = df5.loc[(df5['IP'] == lip)]
        length = dft.shape[0]
        sum = dft['prelabel'].sum() / 5
        if float(sum / length) >alarm_ratio:
            df5['score'].loc[df5['IP'] == lip] = 55

    dfsus1 = df.loc[(df['prelabel'] == 6)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df6 = df.loc[df['IP'].isin(IPsus1)]
    df6['score'] = 0
    for lip in IPsus1:
        dft = df6.loc[(df6['IP'] == lip)]
        length = dft.shape[0]
        sum = dft['prelabel'].sum() / 6
        if float(sum / length) > alarm_ratio:
            df6['score'].loc[df6['IP'] == lip] = 66

    dfAll=pd.concat([df1,df2,df3,df4,df5,df6])
    dfAll.to_csv(outCsvFile)

#---------------------------------------------从中间文件中提取扫描器IP输出到txt文件---------------------------------------
def extractScan(file):
    print('extrct scanIP')
    df = pd.read_csv(file)
    df1 = df.loc[(df['score'] != 0)]
    list1 = df1['IP'].to_list()
    newList = list(set(list1))
    newList.sort()
    i = 1
    f = open(outScannerIPFile, 'w')
    length = len(newList)
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in newList:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1
    f.close()


if __name__=='__main__':
    writeScore(filename)
    extractScan(outCsvFile)













