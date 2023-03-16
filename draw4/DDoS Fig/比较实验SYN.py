import matplotlib

import matplotlib.pyplot as plt

import numpy as np

plt.figure(figsize=(6,6), dpi=80)
# plt.figure(1)

plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号


labels= ['precision','recall','F1','FPR']

first=[100,99.21,99.60,0]
second=[0,0,0,63.78]
third=[1.47,100,2.90,1.33]
# third=[89,67,0]
# first=[0,94,89]
# second=[11,133,67]
# third=[15,262,0]


ax1 = plt.subplot(111)
plt.subplot(111)
plt.tick_params(labelsize=14)
x = np.arange(len(labels)) # x轴刻度标签位置

width = 0.3 # 柱子的宽度

# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中

# x - width，x， x + width即每组数据在x轴上的位置

plt.bar(x - width, first, width, label='RGS',edgecolor='black',hatch='x',lw=1)

plt.bar(x, second, width, label='RUS',edgecolor='black',hatch='/',lw=1)

plt.bar(x + width, third, width, label='False Alarms',edgecolor='black',hatch=' \ ',lw=1)

index=np.arange(len(labels));
font_label = {'family': 'SimHei',
         'weight': 'normal',
         'size': 14,
         }
plt.xlabel('Method',font_label,labelpad=8.5)
plt.ylabel('Number',font_label,labelpad=8.5)
# plt.title('3 datasets')
plt.ylim(0,110)

for a,b in zip(index-width,first):   #柱子上的数字显示
    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=12);
for a,b in zip(index,second):
    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=12);
for a, b in zip(index +width, third):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', fontsize=12);


plt.xticks(x, labels=labels)

plt.legend()



plt.show()
# plt.savefig('compare0121.pdf')
