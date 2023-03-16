import pandas as pd
import csv
from sklearn import tree
from sklearn .tree import DecisionTreeClassifier
from sklearn.metrics import recall_score, precision_score, f1_score, confusion_matrix, accuracy_score, plot_confusion_matrix
file1='scoreNot0 8.csv'
file2='scoreNot0 16.csv'
file3='scoreNot0 32.csv'
file4='scoreNot0 64.csv'

# outfile=file1


def write_metrics(metricfile,metrics_list):
    with open(metricfile, 'a', newline='') as myfile:
        writer = csv.writer(myfile)
        writer.writerow(metrics_list)


def final(file1):
    metric_file=file1+"_metric.csv"
    metric_list=[]

    df = pd.read_csv(file1)
    df['trueLabel']=0
    df['prelabel2']=0
    df['trueLabel'].loc[df['score'] == 11] = 1
    df['prelabel2'].loc[df['prelabel']==1]=1
    metric_list.append(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))
    print(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))

    df['trueLabel'] = 0
    df['prelabel2'] = 0
    df['trueLabel'].loc[df['score'] == 22] = 2
    df['prelabel2'].loc[df['prelabel'] == 2] = 2
    metric_list.append(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))
    print(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))

    df['trueLabel'] = 0
    df['prelabel2'] = 0
    df['trueLabel'].loc[df['score'] == 33] = 3
    df['prelabel2'].loc[df['prelabel'] == 3] = 3
    metric_list.append(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))
    print(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))
    #
    df['trueLabel'] = 0
    df['prelabel2'] = 0
    df['trueLabel'].loc[df['score'] == 44] = 4
    df['prelabel2'].loc[df['prelabel'] == 4] = 4
    metric_list.append(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))
    print(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))

    df['trueLabel'] = 0
    df['prelabel2'] = 0
    df['trueLabel'].loc[df['score'] == 55] = 5
    df['prelabel2'].loc[df['prelabel'] == 5] = 5
    metric_list.append(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))
    print(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))

    df['trueLabel'] = 0
    df['prelabel2'] = 0
    df['trueLabel'].loc[df['score'] == 66] = 6
    df['prelabel2'].loc[df['prelabel'] == 6] = 6
    metric_list.append(precision_score(df['trueLabel'], df['prelabel2'], average='macro'))
    print(precision_score(df['trueLabel'], df['prelabel2'],average='macro'))

    write_metrics(metric_file,metric_list)
    # df.to_csv(file1)

if __name__=='__main__':
    final(file1)
    final(file2)
    final(file3)
    final(file4)
