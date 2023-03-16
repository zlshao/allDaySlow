from sklearn.metrics import mean_squared_error
from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
# X, y = load_iris(return_X_y=True)
trainFile='Trainset/trainset80.csv'
df = pd.read_csv(trainFile)
y = df[['Label22']]
X = df[['protocol','F_Pck','B_Pck','B_Hash_IP','B_Hash_port','F_TCP_S','B_TCP_S']]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
feat_labels = ['protocol','F_Pck','B_Pck','B_Hash_IP','B_Hash_port','F_TCP_S','B_TCP_S']
rf = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1,min_samples_leaf=30)
# rf = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)

rf.fit(x_train, y_train)

y_train_predicted = rf.predict(x_train)
y_test_predicted_full_trees = rf.predict(x_test)
mse_train = mean_squared_error(y_train, y_train_predicted)
mse_test = mean_squared_error(y_test, y_test_predicted_full_trees)
print("RF with full trees, Train MSE: {} Test MSE: {}".format(mse_train, mse_test))
# y = data[['Label22']]
# X = data[['protocol','F_Pck','B_Pck','B_Hash_IP','B_Hash_port','F_TCP_S','B_TCP_S']]
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]
for f in range(x_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, feat_labels[indices[f]], importances[indices[f]]))




# print(X)
# print(X.shape)
#
# lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X, y)
# model = SelectFromModel(lsvc, prefit=True)
# X_new = model.transform(X)
# print(X_new)
# print(X_new.shape)
#
