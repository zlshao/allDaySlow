import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
import joblib

trainFile='Trainset/trainset80.csv'
testFile= "testsetLabeled 64.csv"

def writeprelabel(filename,prelabel):
    df = pd.read_csv(filename)
    df['prelabel'] = prelabel
    df.to_csv(filename, index=None)

def detect():
    data = pd.read_csv(trainFile)
    train_y = data[['Label22']]
    train_x = data[['protocol','F_Pck','B_Pck','B_Hash_IP','B_Hash_port','F_TCP_S','B_TCP_S']]

    data_test=pd.read_csv(testFile)

    test_x = data_test[['protocol','F_Pck','B_Pck','B_Hash_IP','B_Hash_port','F_TCP_S','B_TCP_S']]


    clf = joblib.load("SDSDetector.pkl")

    y_predict = clf.predict(test_x)
    writeprelabel(testFile, y_predict)

if __name__=='__main__':
    detect()

