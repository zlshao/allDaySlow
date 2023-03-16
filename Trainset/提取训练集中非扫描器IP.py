import pandas as pd

filename='trainset80.csv'
outtxt='训练集非扫描器列表.txt'
def extract(filename):
    IPlist=[]
    df = pd.read_csv(filename)
    dfAll=[]
    dfAll.extend(df['IP'].to_list())
    dfAll=list(set(dfAll))
    print('所有IP的个数： '+str(len(dfAll)))


    dfPre = df.loc[(df['Label22'] != 0)]
    IPlist.extend(dfPre['IP'].to_list())
    IPlist=list(set(IPlist))
    print('扫描IP数： '+str(len(IPlist)))

    IPFinal=set(dfAll)-set(IPlist)
    IPFinal = list(set(IPFinal))
    print('最终IP数： '+str(len(IPFinal)))

    i = 1
    f = open(outtxt, 'w')
    length = len(IPFinal)
    # f.write('TCP mixed =' + str(length) + ';\n')
    f.write('Ext_Count =' + str(length) + ';\n')
    for l in IPFinal:
        wt1 = 'Ext_IP' + str(i) + '="' + l + '";\n'
        f.write(wt1)
        i += 1

if __name__=='__main__':
    extract(filename)