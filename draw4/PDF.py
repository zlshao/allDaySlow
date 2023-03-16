import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

sns.set(palette="muted", color_codes=True)
matplotlib.rcParams['font.sans-serif'] = ['SimHei']     # 显示中文
# 为了坐标轴负号正常显示。matplotlib默认不支持中文，设置中文字体后，负号会显示异常。需要手动将坐标轴负号设为False才能正常显示负号。
matplotlib.rcParams['axes.unicode_minus'] = False


#sns.set_style({"font.sans-serif": ['simhei', 'Droid Sans Fallback']})
# matplotlib.rcParams['axes.unicode_minus'] = False     # 正常显示负号
#matplotlib.rcParams['font.sans-serif'] = ['SimHei']   # 用黑体显示中文
from matplotlib.pyplot import MultipleLocator

data = pd.read_csv('hash16_bit_Distri_FarmHash.csv')
dv = data[['bitC15']]
sns.distplot(dv, color='#3CB371', bins=100, hist=True)
plt.ylabel('概率密度')
plt.xlabel("互异key的数量")
#x_major_locator=MultipleLocator(10)
plt.xlim(0,200)
plt.show()
# plt.savefig('PDF16.pdf')