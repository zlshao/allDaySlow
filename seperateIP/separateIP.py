import string

import pandas as pd
import numpy as np

# from extractIPFromFile import place

csvFile='modi/modi.csv'
# out1='0603 bit8/path 16 bit8.csv'
# out2='0603 bit8/path 32 bit8.csv'
# out3='0603 bit8/path 64 bit8.csv'
# out4='0603 bit8/path 128 bit8.csv'
#
#
# txt1='0603 bit8/0603 16 bit8.txt'
# txt2='0603 bit8/0603 32 bit8.txt'
# txt3='0603 bit8/0603 64 bit8.txt'
# txt4='0603 bit8/0603 128 bit8.txt'

txt1='MWSM70 50 30  100.txt'
txt2='MWSM63 25 18  100.txt'
txt3='MWSM62 50 40  100.txt'
txt4='MWSM70 50 30  100.txt'


out1=txt1+'.csv'
out2=txt2+'.csv'
out3=txt3+'.csv'
out4=txt4+'.csv'



str1='='
str2=';'

def seperate(txt,outcsv):
    df=pd.read_csv(csvFile,index_col=False)
    txt_tables = []
    f = open(txt, "r", encoding='utf-8')
    line = f.readline().splitlines()  # 读取第一行
    while line:
        txt_tables.extend(line)  # 列表增加
        line = f.readline().splitlines()  # 读取下一行
    print(type(txt_tables[0]))
    ip=[]
    for str in txt_tables:
        loc1=str.find(str1)
        loc2=str.find(str2)
        substr=str[loc1+2:loc2-1]
        if len(substr)>20: #ipv6地址
            substr=substr.replace(':','_')
            # print(substr)
        # temp='201904090000.pcap.CONN.pcap.Mixed_rseed-2222.pcap.'+substr+'.pcap'
        temp='202006031400.pcap.Mixed_rseed-2222.pcap.'+substr+'.pcap'

        ip.append(temp)
    # print(ip)
    ip.sort()
    dfout=df.loc[(df['file'].isin(ip))]

    print((df['file']))
    dfout.to_csv(outcsv)

if __name__=='__main__':
    seperate(txt1,out1)
    # seperate(txt2,out2)
    # seperate(txt3,out3)
    # seperate(txt4,out4)
    #













