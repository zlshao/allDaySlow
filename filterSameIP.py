import numpy as np
import pandas as pd
import csv
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

filename= 'testsetLabeled 8.csv'
outfile='1224Vote 8.txt'

def filter(file):

    df=pd.read_csv(file)
    # df1 = df.loc[(df['Label'] == 4) |(df['Label'] == 18 )|(df['Label'] == 2)|(df['Label'] == 15)|(df['Label'] == 32)]
    df1 = df.loc[(df['score']!=0)]
    # df1 = df.loc[(df['prelabel'] !=0)]
    list1=df1['IP'].to_list()
    print(list1)
    newList=list(set(list1))
    newList.sort()
    i=1
    f = open(outfile, 'w')
    length=len(newList)
    f.write('Ext_Count ='+str(length)+';\n' )
    for l in newList:
        wt1='Ext_IP'+str(i)+'="'+l+'";\n'
        f.write(wt1)
        i+=1
    f.close()
    # print(newList)


if __name__ == '__main__':
    filter(filename)