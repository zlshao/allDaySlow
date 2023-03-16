import pandas as pd
import os
import csv

path="testsetLabeled 8.csv"

outfile='prelabelEqual123456.csv'
outtxt='singleIP 8 1224.txt'

def extract(filelist):

    df=pd.read_csv(path)
    df=df.loc[(df['prelabel']!=0)]
    df.to_csv(outfile,index=None,mode='a', header=False)

    df1 = pd.read_csv(outfile, header=None, names=['Unnamed: 0','protocol','IP','ID','Time','F_Pck','B_Pck','F_Hash_IP','B_Hash_IP','F_Hash_port','B_Hash_port','F_TCP_S','B_TCP_S','Label22','prelabel'])
    df1.to_csv(outfile, index=False)

def distin(path):
    df=pd.read_csv(path)

    df1 = df.loc[(df['score'] ==11)]
    # df1 = df.loc[(df['prelabel'] !=0)]
    list1 = df1['IP'].to_list()
    print("TCP netscan:")
    newList = list(set(list1))
    newList.sort()
    i = 1
    f = open(outtxt, 'w')
    length = len(newList)
    f.write('TCP netscan =' + str(length) + ';\n')
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in newList:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1

    df2= df.loc[(df['score'] ==22)]
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

    df2= df.loc[(df['score'] ==33)]
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

    df2= df.loc[(df['score'] ==44)]
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

    df2= df.loc[(df['score'] ==55)]
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

    df2= df.loc[(df['score'] ==66)]
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


if __name__ == '__main__':

    # extract(path)
    distin(path)