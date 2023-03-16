# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:05:48 2020

@author: yss
"""

import matplotlib.pyplot as plt #导入Matplotlib
from matplotlib.ticker import MaxNLocator
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

x  =['35','50','65','80','100'] #此处也可数字
y1 =[4,3,2,2,1]
y2 =[9,6,5,4,3]
y3 =[12,8,5,5,4]
y4 =[17,12,7,7,6]

plt.figure(figsize = (12, 12)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y1, 'r-',label = 'n=5000',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, 'g--', label = 'n=10000', linewidth = 2.5)
plt.plot(x, y3, 'b-.', label = 'n=15000', linewidth = 2.5)
plt.plot(x, y4, 'k:', label = 'n=20000', linewidth = 2.5)

plt.plot(x, y1, 'or',markersize = 8) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, '*g',markersize = 8)
plt.plot(x, y3, 'Db',markersize = 8)
plt.plot(x, y4, '^k',markersize = 8)

ax = plt.subplot(111) #这是画布哦，说明只在一张图显示，也可分割多图
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)

plt.xlabel('Threshold ', fontsize=24) # x轴名称
plt.ylabel('Number of Records', fontsize=24) # y轴名称
# plt.title('A Simple Example') #标题
plt.ylim(0, 20) #显示的y轴范围
plt.legend(fontsize=20) #显示图例

plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.show() #显示作图结果

