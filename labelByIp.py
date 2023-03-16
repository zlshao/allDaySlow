# 把聚类后的CSV 扫描流量打标签为1 其他流量标记为0 tcp


from operator import itemgetter
import csv
import numpy as np
import pandas as pd


def labelFile():
    filename = 'Testset/202006031400.pcap.Mixed_rseed-2222.pcap.bit_31.thre_80.ratio_8.IP.csv'  # tcp
    print("Label begin")
    # input_file = open(filename)
    output_file = "testsetLabeled 0603 hash16 8.csv"

    df1 = pd.read_csv(filename,usecols=['protocol','IP','ID','Time','F_Pck','B_Pck','B_Hash_IP','B_Hash_port','F_TCP_S','B_TCP_S'])



    df1['Label22']=0
    print(df1)

    df1['Label22'].loc[df1['IP'].isin(['192.1.1.1','192.1.1.2','192.1.1.3','192.1.1.4','192.1.1.5'])] = 1 #netscan
    df1['Label22'].loc[df1['IP'].isin(
        ['192.2.2.1','192.2.2.2','192.2.2.3','192.2.2.4','192.2.2.5'])] = 2  # portscan
    df1['Label22'].loc[df1['IP'].isin(['192.3.3.1','192.3.3.2','192.3.3.3','192.3.3.4','192.3.3.5'])] = 3 #mixedscan
    df1['Label22'].loc[df1['IP'].isin(['192.4.4.1','192.4.4.2','192.4.4.3','192.4.4.4','192.4.4.5'])] = 4  # netscan
    df1['Label22'].loc[df1['IP'].isin(['192.5.5.1','192.5.5.2','192.5.5.3','192.5.5.4','192.5.5.5'])] = 5 #portscan
    df1['Label22'].loc[df1['IP'].isin(['192.6.6.1','192.6.6.2','192.6.6.3','192.6.6.4','192.6.6.5'])] = 6  # mixedscan

    # df1[None] = df1[None].str.replace('\n', '')
    df1.to_csv(output_file)
    print('Label  end')


if __name__=='__main__':
    labelFile()






