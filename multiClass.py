
#--------------------检测端口扫描，输出扫描器IP列表以及中间文件-----------


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.cluster import KMeans

#----------------------------------------------输入文件和输出文件------------------------------------------
trainFile='Trainset/trainset80.csv'
filename="Testset/202006031400.pcap.Mixed_rseed-2222.pcap.bit_25.thre_80.ratio_16.IP.csv"  #输入文件,测试集
outCsvFile='output/midFile/outMid_'+filename[8:]      #中间输出文件
outScannerIPFile1='output/txtFile/outScanner_'+filename[8:]+'_distinct.txt'  #输出扫描器IP地址,分类
outScannerIPFile2='output/txtFile/outScanner_'+filename[8:]+'_all.txt' #输出扫描器IP地址，不分类

#---------------------------------------------将预测标签写入测试集-----------------------------------------
def writeprelabel(filename,prelabel):
    df = pd.read_csv(filename,index_col=False)
    df['prelabel'] = prelabel
    df.to_csv(filename, index=None)

#---------------------------------------------加载分类器进行分类-------------------------------------------
def detect():
    data = pd.read_csv(trainFile,index_col=False)
    train_y = data[['Label22']]
    train_x = data[['protocol','F_Pck','B_Pck','B_Hash_IP','B_Hash_port','F_TCP_S','B_TCP_S']]

    data_test = pd.read_csv(filename,index_col=False)
    test_x = data_test[['protocol','F_Pck','B_Pck','B_Hash_IP','B_Hash_port','F_TCP_S','B_TCP_S']]
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=10, min_samples_leaf=1, random_state=None,
                                 splitter='best')  # ,random_state=99

    clf = clf.fit(train_x, train_y)
    y_predict = clf.predict(test_x)
    print(y_predict)
    writeprelabel(filename, y_predict)
#-------------------------------返回列表的众数-----------------
def getZhongShu(arr):
    if len(arr)==1:
        return arr[0]
    candi=arr[0]
    vote=1
    for i in arr:
        if i==candi:
            vote+=1
        else:
            vote-=1
            if vote<0:
                candi=i
                vote=1
    if vote==0:
        return 0
    else:
        return candi

#-----------------------------------------根据报警比例进行筛选输出到中间文件----------------------------------


def writeScore(filename):
    df = pd.read_csv(filename)
    dfsus1=df.loc[(df['prelabel'] ==1)]
    IPsus1=dfsus1['IP'].to_list()
    IPsus1=list(set(IPsus1))
    df1=df.loc[df['IP'].isin(IPsus1)]
    df1.loc[:,'score']=0
    for lip in IPsus1:
        dft = df1.loc[(df1['IP'] == lip)]
        arr=dft['prelabel'].to_list()
        df1['score'].loc[df1['IP'] == lip]=getZhongShu(arr)*11


    dfsus1=df.loc[(df['prelabel'] ==2)]
    IPsus1=dfsus1['IP'].to_list()
    IPsus1=list(set(IPsus1))
    df2=df.loc[df['IP'].isin(IPsus1)]
    # df2.loc[:,'score']=0
    # for lip in IPsus1:
    #     dft = df2.loc[(df2['IP'] == lip)]
    #     arr = dft['prelabel'].to_list()
    #     df2['score'].loc[df2['IP'] == lip] = getZhongShu(arr) * 11


    dfsus1 = df.loc[(df['prelabel'] == 3)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df3 = df.loc[df['IP'].isin(IPsus1)]
    df3.loc[:,'score'] = 0
    for lip in IPsus1:
        dft = df3.loc[(df3['IP'] == lip)]
        arr = dft['prelabel'].to_list()
        df3['score'].loc[df3['IP'] == lip] = getZhongShu(arr) * 11

    dfsus1 = df.loc[(df['prelabel'] == 4)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df4 = df.loc[df['IP'].isin(IPsus1)]
    df4.loc[:,'score'] = 0
    for lip in IPsus1:
        dft = df4.loc[(df4['IP'] == lip)]
        arr = dft['prelabel'].to_list()
        df4['score'].loc[df4['IP'] == lip] = getZhongShu(arr) * 11


    dfsus1 = df.loc[(df['prelabel'] == 5)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df5 = df.loc[df['IP'].isin(IPsus1)]
    # df5.loc[:,'score'] = 0
    # for lip in IPsus1:
    #     dft = df5.loc[(df5['IP'] == lip)]
    #     arr = dft['prelabel'].to_list()
    #     df5['score'].loc[df5['IP'] == lip] = getZhongShu(arr) * 11


    dfsus1 = df.loc[(df['prelabel'] == 6)]
    IPsus1 = dfsus1['IP'].to_list()
    IPsus1 = list(set(IPsus1))
    df6 = df.loc[df['IP'].isin(IPsus1)]
    df6.loc[:,'score'] = 0
    for lip in IPsus1:
        dft = df6.loc[(df6['IP'] == lip)]
        arr = dft['prelabel'].to_list()
        df6['score'].loc[df6['IP'] == lip]  = getZhongShu(arr) * 11


    dfAll=pd.concat([df1,df2,df3,df4,df5,df6])

    dfAll.to_csv(outCsvFile,index=None)

#-------------------提取扫描器IP，全部的，方便提取pcap--------------------
def extractScanAll(file):
    print('extrct scanIP')
    df = pd.read_csv(file)
    df1 = df.loc[(df['score'] != 0)]
    list1 = df1['IP'].to_list()
    newList = list(set(list1))
    newList.sort() #扫描器IP列表
    i = 1
    f = open(outScannerIPFile2, 'w')
    length = len(newList)
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in newList:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1
    f.close()

#---------------------------------------------从中间文件中提取扫描器IP输出到txt文件---------------------------------------
def extractScan(file):
    print('extract scanIP')
    df = pd.read_csv(file,index_col=None)

    df1 = df.loc[(df['score'] == 11)]
    # df1 = df.loc[(df['prelabel'] !=0)]
    list1 = df1['IP'].to_list()
    print("TCP netscan:")
    newList = list(set(list1))
    newList.sort()
    i = 1
    f = open(outScannerIPFile1, 'w')
    length = len(newList)
    f.write('TCP netscan =' + str(length) + ';\n')
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in newList:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1

    df2 = df.loc[(df['score'] == 22)]
    # df1 = df.loc[(df['prelabel'] !=0)]
    list1 = df2['IP'].to_list()
    print("TCP netscan:")
    newList = list(set(list1))
    newList.sort()
    i = 1
    # f = open(outtxt, 'w')
    length = len(newList)
    f.write('TCP port =' + str(length) + ';\n')
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in newList:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1

    df2 = df.loc[(df['score'] == 33)]
    # df1 = df.loc[(df['prelabel'] !=0)]
    list1 = df2['IP'].to_list()
    print("TCP mixed:")
    newList = list(set(list1))
    newList.sort()
    i = 1
    # f = open(outtxt, 'w')
    length = len(newList)
    f.write('TCP mixed =' + str(length) + ';\n')
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in newList:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1

    df2 = df.loc[(df['score'] == 44)]
    # df1 = df.loc[(df['prelabel'] !=0)]
    list1 = df2['IP'].to_list()
    # print("UDP portscan:")
    newList = list(set(list1))
    newList.sort()
    i = 1
    # f = open(outtxt, 'w')
    length = len(newList)
    f.write('Udp net =' + str(length) + ';\n')
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in newList:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1

    df2 = df.loc[(df['score'] == 55)]
    # df1 = df.loc[(df['prelabel'] !=0)]
    list1 = df2['IP'].to_list()
    # print("UDP portscan:")
    newList = list(set(list1))
    newList.sort()
    i = 1
    # f = open(outtxt, 'w')
    length = len(newList)
    f.write('UDP port =' + str(length) + ';\n')
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in newList:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1

    df2 = df.loc[(df['score'] == 66)]
    # df1 = df.loc[(df['prelabel'] !=0)]
    list1 = df2['IP'].to_list()
    # print("UDP portscan:")
    newList = list(set(list1))
    newList.sort()
    i = 1
    # f = open(outtxt, 'w')
    length = len(newList)
    f.write('UDP mixed =' + str(length) + ';\n')
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in newList:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1

    f.close()


def clusterData(filename, k):
        df1 = pd.read_csv(filename, index_col=None)
        df2 = df1[['prelabel', 'score', 'protocol']]
        km = KMeans(n_clusters=k)
        kLabel = km.fit_predict(df2)
        df1['kLabel'] = kLabel
        print(df1)
        df1.to_csv(filename, index=None)


if __name__=='__main__':
    detect()
    writeScore(filename)
    extractScan(outCsvFile)
    extractScanAll(outCsvFile)

