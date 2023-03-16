
#------------对有监督学习后的扫描器聚类，特征为：------------
# 1、协议  2、标签  3、目的端口号/目的IP
#水平扫描: 目的端口号
#垂直扫描： 目的IP
#混合扫描： 目的IP前缀


import numpy as np
import pandas as pd
import csv
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import time

fname_Mid='output/midFile/outMid_202006031400.pcap.Mixed_rseed-2222.pcap.bit_25.thre_80.ratio_32.IP.csv'
fname_PP='202006031400.pcap.Mixed_rseed-2222.pcap.bit_25.thre_80.ratio_32.IPP.csv'
fname_PDpt='202006031400.pcap.Mixed_rseed-2222.pcap.bit_25.thre_80.ratio_32.IPA_TB.csv'

outKmeansPP='output/kmeansFile/outKmeansPP_'+fname_PP
outKmeansPDpt='output/kmeansFile/outKmeansPDpt_'+fname_PDpt



dfInfilePP=pd.read_csv(fname_PP,index_col=False)
dfInfilePDpt=pd.read_csv(fname_PDpt,index_col=False)



def extractPdpt(f_mid): #相同的目的端口
    df=pd.read_csv(f_mid,index_col=False)
    dfKmeansPDpt = pd.DataFrame()  # 存放需要聚类的扫描器特征列表
    dfsus = df.loc[(df['score'] == 11)]
    IPsus = dfsus['IP'].to_list()
    IPsus = list(set(IPsus))
    dfTemp1=dfInfilePDpt.loc[dfInfilePDpt['IP_a'].isin(IPsus)]
    dfTemp1['label']=1
    dfKmeansPDpt=dfKmeansPDpt.append(dfTemp1)
    # print(dfTemp1)

    dfsus = df.loc[(df['score'] == 44)]
    IPsus = dfsus['IP'].to_list()
    IPsus = list(set(IPsus))
    dfTemp2=dfInfilePDpt.loc[dfInfilePDpt['IP_a'].isin(IPsus)]
    dfTemp2['label']=4
    dfKmeansPDpt=dfKmeansPDpt.append(dfTemp2)

    dfKmeansPDpt.to_csv(outKmeansPDpt,index=False)

def extractPP(f_mid): #相同的目的IP地址
    df = pd.read_csv(f_mid, index_col=False)
    dfKmeansPP = pd.DataFrame()  # 存放需要聚类的扫描器特征列表
    dfsus = df.loc[(df['score'] == 22)]
    IPsus = dfsus['IP'].to_list()
    IPsus = list(set(IPsus))
    dfTemp = dfInfilePP.loc[dfInfilePP['IP_a'].isin(IPsus)]
    dfTemp['label'] = 2
    dfKmeansPP=dfKmeansPP.append(dfTemp)

    dfsus = df.loc[(df['score'] == 55)]
    IPsus = dfsus['IP'].to_list()
    IPsus = list(set(IPsus))
    dfTemp = dfInfilePP.loc[dfInfilePP['IP_a'].isin(IPsus)]
    dfTemp['label'] = 5
    dfKmeansPP=dfKmeansPP.append(dfTemp)


    dfsus = df.loc[(df['score'] == 33)] #TCP混合扫描
    IPsus = dfsus['IP'].to_list()
    IPsus = list(set(IPsus))
    dfTemp = dfInfilePP.loc[dfInfilePP['IP_a'].isin(IPsus)]
    dfTemp['label'] = 3
    dfKmeansPP = dfKmeansPP.append(dfTemp)

    dfsus = df.loc[(df['score'] == 66)] #UDP混合扫描
    IPsus = dfsus['IP'].to_list()
    IPsus = list(set(IPsus))
    dfTemp = dfInfilePP.loc[dfInfilePP['IP_a'].isin(IPsus)]
    dfTemp['label'] = 6
    dfKmeansPP = dfKmeansPP.append(dfTemp)

    dfKmeansPP.to_csv(outKmeansPP,index=False)

def getPrefix(str): #按ABC类网络取前缀
    tmp = str.split('.', 2)
    if len(tmp)<2:
        return '0'
    ret=tmp[0]+tmp[1]
    return ret

def getPreFix2(str,num): #按超网划分取得前缀，num可以自主选择,比如24
    list1 = str.split('.')
    list2 = []
    for item in list1:
        item = bin(int(item))
        # 去掉每段二进制前的0b.
        item = item[2:]
        # 将IP地址地址的每个字段转换成八位，不足的在每段前补0.
        list2.append(item.zfill(8))

    # 将4段8位二进制连接起来，变成32个0101的样子.
    v2 = ''.join(list2)  # v2是字符串的类型
    # v3 = int(v2,base=2) #转换成10进制
    v2=v2[0:num]
    return v2

#----------------------聚类：垂直扫描、混合扫描-------------------------
def clusterDataPP(filename,k1,k2,k3,k4): #对filename中的特征聚类，按目的IP聚类
    df1=pd.read_csv(filename,index_col=False)
    dfVert= df1.loc[(df1['label'] ==2)|(df1['label'] ==5)]
    dfMixed= df1.loc[(df1['label'] ==3)|(df1['label'] ==6)]

    dfv6=dfVert.loc[(dfVert['protocol'] ==6)]
    dfv17= dfVert.loc[(dfVert['protocol'] == 17)]

    dfm6=dfMixed.loc[(dfMixed['protocol'] ==6)]
    dfm17= dfMixed.loc[(dfMixed['protocol'] == 17)]
    #-------------垂直扫描聚类：按目的IP

    dfTmp1=dfv6[['label','IP_b','protocol']]
    dfTmp1['hashText']=dfTmp1['IP_b'].map(hash) #将文本型的IP哈希转换成数字
    dfTmp1=dfTmp1[['label','protocol','hashText']]
    km=KMeans(n_clusters=k1)
    kLabel=km.fit_predict(dfTmp1)
    dfv6['hashText']=dfTmp1['hashText']
    dfv6['kLabel']=kLabel

    dfTmp1=dfv17[['label','IP_b','protocol']]
    dfTmp1['hashText']=dfTmp1['IP_b'].map(hash) #将文本型的IP哈希转换成数字
    dfTmp1=dfTmp1[['label','protocol','hashText']]
    km=KMeans(n_clusters=k2)
    kLabel=km.fit_predict(dfTmp1)
    dfv17['hashText']=dfTmp1['hashText']
    dfv17['kLabel']=kLabel
    # dfv17['kLabel']=dfv17['kLabel'].map(lambda x:x+k)
    # print(df2)

    #-------------混合扫描聚类：按目的IP前缀聚合
    dfTmp2=dfm6[['label','IP_b','protocol']]
    dfTmp2['IP_b']=dfTmp2['IP_b'].map(getPrefix) #取前缀
    # print(dfTmp2)
    dfTmp2['hashText']=dfTmp2['IP_b'].map(hash) #将文本型的IP哈希转换成数字
    dfTmp2=dfTmp2[['label','protocol','hashText']]
    km=KMeans(n_clusters=k3)
    kLabel=km.fit_predict(dfTmp2)
    dfm6['kLabel']=kLabel
    dfm6['hashText']=dfTmp2['hashText']
    # dfm6['kLabel']=dfm6['kLabel'].map(lambda x:x+2*k)

    dfTmp2=dfm17[['label','IP_b','protocol']]
    dfTmp2['IP_b']=dfTmp2['IP_b'].map(getPrefix) #取前缀
    # print(dfTmp2)
    dfTmp2['hashText']=dfTmp2['IP_b'].map(hash) #将文本型的IP哈希转换成数字
    dfTmp2=dfTmp2[['label','protocol','hashText']]
    km=KMeans(n_clusters=k4)
    kLabel=km.fit_predict(dfTmp2)
    dfm17['kLabel']=kLabel
    dfm17['hashText']=dfTmp2['hashText']
    # dfm17['kLabel']=dfm17['kLabel'].map(lambda x:x+3*k)


    df1=pd.concat([dfv6,dfv17,dfm6,dfm17])
    df1.to_csv(filename,index=False)

#-------------------------聚类：水平扫描-----------------------------
def clusterDataPDpt(filename,k1,k2): #对filename中的特征聚类，按端口聚类
    df1=pd.read_csv(filename,index_col=False)

    dfTcp= df1.loc[(df1['protocol'] == 6)]
    dfUdp= df1.loc[(df1['protocol'] == 17)]

    dfTmp1=dfTcp[['label','port_b','protocol','F_Len_Avg']]
    km=KMeans(n_clusters=k1)
    kLabel=km.fit_predict(dfTmp1)
    dfTcp['kLabel']=kLabel
    # print(dfTcp)

    dfTmp2=dfUdp[['label','port_b','protocol','F_Len_Avg']]
    km=KMeans(n_clusters=k2)
    kLabel=km.fit_predict(dfTmp2)
    dfUdp['kLabel']=kLabel
    # dfUdp['kLabel']= dfUdp['kLabel'].map(lambda x:x+k)
    # print(dfUdp)

    df1=pd.concat([dfTcp,dfUdp])
    df1.to_csv(filename,index=False)

#-----------------输出各个扫描集群的IP地址
def finalClusterRes(filename):
    df = pd.read_csv(filename, index_col=False)

    df1=df.loc[(df['label'])==1]
    kList=df1['kLabel'].to_list()  #聚类标签
    kList=list(set(kList))
    k=len(kList)
    print('TCP水平扫描：')
    print('共'+str(k)+'个扫描器集群')
    outputCluster(df1,kList)

    df1 = df.loc[(df['label']) == 2]
    kList = df1['kLabel'].to_list()  # 聚类标签
    kList = list(set(kList))
    k = len(kList)
    print('TCP垂直扫描：')
    print('共' + str(k) + '个扫描器集群')
    outputCluster(df1, kList)

    df1 = df.loc[(df['label']) == 3]
    kList = df1['kLabel'].to_list()  # 聚类标签
    kList = list(set(kList))
    k = len(kList)
    print('TCP混合扫描：')
    print('共' + str(k) + '个扫描器集群')
    outputCluster(df1, kList)

    df1 = df.loc[(df['label']) == 4]
    kList = df1['kLabel'].to_list()  # 聚类标签
    kList = list(set(kList))
    k = len(kList)
    print('UDP水平扫描：')
    print('共' + str(k) + '个扫描器集群')
    outputCluster(df1, kList)

    df1 = df.loc[(df['label']) == 5]
    kList = df1['kLabel'].to_list()  # 聚类标签
    kList = list(set(kList))
    k = len(kList)
    print('UDP垂直扫描：')
    print('共' + str(k) + '个扫描器集群')
    outputCluster(df1, kList)

    df1 = df.loc[(df['label']) == 6]
    kList = df1['kLabel'].to_list()  # 聚类标签
    kList = list(set(kList))
    k = len(kList)
    print('UDP混合扫描：')
    print('共' + str(k) + '个扫描器集群')
    outputCluster(df1, kList)





def outputCluster(df,kList):
    count = 1
    for i in kList:
        dfTmp = df.loc[(df['kLabel'] == i)]
        ipList = dfTmp['IP_a'].to_list()
        ipList = list(set(ipList))
        sorted(ipList)
        if len(ipList) == 0:
            continue
        if len(ipList) == 1:
            print('单扫描器 —— 共 ' + str(len(ipList)) + ' 个扫描器： ')
            print(ipList)
        else:
            print('扫描集群 —— 共 ' + str(len(ipList)) + ' 个扫描器： ')
            print(ipList)
        print()
        count += 1


if __name__=='__main__':
    k1=25
    k2=6
    k3=6
    k4=6
    k5=6
    k6=1

    start=time.perf_counter()
    extractPP(fname_Mid)
    clusterDataPP(outKmeansPP,k2,k5,k3,k6)
    finalClusterRes(outKmeansPP)

    extractPdpt(fname_Mid)
    clusterDataPDpt(outKmeansPDpt,k1,k4)
    finalClusterRes(outKmeansPDpt)

    end=time.perf_counter()

    print('聚类的时间为： %s Seconds' % (end - start))





