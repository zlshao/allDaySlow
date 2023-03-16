import  matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']     # 显示中文
# 为了坐标轴负号正常显示。matplotlib默认不支持中文，设置中文字体后，负号会显示异常。需要手动将坐标轴负号设为False才能正常显示负号。
matplotlib.rcParams['axes.unicode_minus'] = False

sample_x=['1/8','1/16','1/32','1/64']
pckrate_y=[2.7,4.8,7.2,10.0]
throughput_y=[26.1,45.8,69.5,96.3]

plt.figure(figsize=(5,5))

plt.bar(sample_x,pckrate_y,width=0.4,color='#006D87',edgecolor='#006D87')
plt.xlabel('抽样率',fontsize=12)
plt.ylabel('包速率(Mpps)',fontsize=12)
plt.ylim(0,12)
plt.xticks(fontsize=12)#嗯调调字体
plt.yticks(fontsize=12)
for a, b in zip(sample_x, pckrate_y):
 plt.text(a, b, '%.1f' % b, ha='center', va='bottom', fontsize=12)
plt.savefig('SDS Perfor1.pdf')


# plt.bar(sample_x,throughput_y,width=0.4,color='#5DA39D',edgecolor='#5DA39D')
# plt.xlabel('抽样率',fontsize=12)
# plt.ylabel('比特率(Gbps)',fontsize=12)
# plt.ylim(0,105)
# plt.xticks(fontsize=12)#嗯调调字体
# plt.yticks(fontsize=12)
# for a, b in zip(sample_x, throughput_y):
#  plt.text(a, b, '%.1f' % b, ha='center', va='bottom', fontsize=12)


# plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2)

plt.show()
# plt.savefig('SDS Perfor2.pdf')
