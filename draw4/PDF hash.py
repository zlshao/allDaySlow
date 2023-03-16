import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
# sns.set(palette="muted", color_codes=True)
# #sns.set_style({"font.sans-serif": ['simhei', 'Droid Sans Fallback']})
# matplotlib.rcParams['axes.unicode_minus'] = False     # 正常显示负号
#matplotlib.rcParams['font.sans-serif'] = ['SimHei']   # 用黑体显示中文
from matplotlib.pyplot import MultipleLocator

data = pd.read_csv('hashPDF/0.csv',index_col=False)
dv = data[['B_Hash_IP']]
# sns.distplot(dv, color='#3CB371', bins=15, hist=True)
# plt.ylabel('Probability Density')
# plt.xlabel("Different Keys")
# #x_major_locator=MultipleLocator(10)


# kwargs = {'cumulative': True}
# sns.distplot(dv, hist_kws=kwargs, kde_kws=kwargs)
fig,ax0 = plt.subplots(nrows=1,figsize=(6,6))
#第二个参数是柱子宽一些还是窄一些，越大越窄越密
ax0.hist(dv,10,density=1,histtype='bar',facecolor='yellowgreen',alpha=0.75)
plt.xlim(0,18)
plt.show()
# plt.savefig('PDF8.pdf')