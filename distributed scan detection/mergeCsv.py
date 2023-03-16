import pandas as pd
import os
import csv

#--------------合并某路径下多个CSV文件,输出合并后的csv-------
#--------------------改两个文件名--------------------

if __name__=='__main__':
    path = 'output/files_IPDpt/'
    newData=pd.DataFrame()
    allFiles=[]
    for root, dirs, files in os.walk(path):
        allFiles.append(files)



    for fname in files:
            if 'csv' in fname:
                fname_path = path + fname
                cur = pd.read_csv(fname_path,index_col=False)

                print('正在合并：   '+fname_path)

                newData=newData.append(cur)

    excel_name = 'output/output_IPDpt.csv' #输出的文件
    # excel_name = 'output/output_IPP.csv'
    # excel_name = 'output/output_IPDpt.csv'
    newData.to_csv(excel_name) #写的时候忽略默认索引
