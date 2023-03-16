# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:05:48 2020

@author: yss
"""

import matplotlib.pyplot as plt #导入Matplotlib

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

x  =['1/8','1/16','1/32','1/64','1/128'] #此处也可数字
y1 =[18,9,4,1,1]
y2 =[37,18,9,5,2]
y3 =[52,25,12,7,3]
y4 =[70,35,17,9,4]

xx  =['35','50','65','80','100'] #此处也可数字
y11 =[4,3,2,2,1]
y22 =[9,6,5,4,3]
y33 =[12,8,5,5,4]
y44 =[17,12,7,7,6]

plt.figure(figsize=(30,14),dpi=200)

plt.subplot(1,2,1) #这是画布哦，说明只在一张图显示，也可分割多图
plt.xticks(fontsize=20)#嗯调调字体
plt.yticks(fontsize=20)
# plt.figure(figsize = (16, 8)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y1, 'r-',label = 'n=5000',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, 'g--', label = 'n=10000', linewidth = 2.5)
plt.plot(x, y3, 'b-.', label = 'n=15000', linewidth = 2.5)
plt.plot(x, y4, 'k:', label = 'n=20000', linewidth = 2.5)

plt.plot(x, y1, 'or',markersize = 8) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, '*g',markersize = 8)
plt.plot(x, y3, 'Db',markersize = 8)
plt.plot(x, y4, '^k',markersize = 8)
plt.xlabel('Sampling Rate ', fontsize=25) # x轴名称
plt.ylabel('Number of Records', fontsize=25) # y轴名称
# plt.title('A Simple Example') #标题
plt.ylim(0, 72) #显示的y轴范围
# plt.legend(fontsize=20) #显示图例

plt.subplot(1,2,2)#这是画布哦，说明只在一张图显示，也可分割多图
# plt.figure(figsize = (16, 8)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(xx, y11, 'r-',label = 'n=5000',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(xx, y22, 'g--', label = 'n=10000', linewidth = 2.5)
plt.plot(xx, y33, 'b-.', label = 'n=15000', linewidth = 2.5)
plt.plot(xx, y44, 'k:', label = 'n=20000', linewidth = 2.5)

plt.plot(xx, y11, 'or',markersize = 8) #作图，设置标签、线条颜色、线条大小
plt.plot(xx, y22, '*g',markersize = 8)
plt.plot(xx, y33, 'Db',markersize = 8)
plt.plot(xx, y44, '^k',markersize = 8)

# ax2 = plt.subplot(122) #这是画布哦，说明只在一张图显示，也可分割多图
plt.xticks(fontsize=20)#嗯调调字体
plt.yticks(fontsize=20)

plt.xlabel('Threshold ', fontsize=25) # x轴名称
plt.ylabel('Number of Records', fontsize=25) # y轴名称
# plt.title('A Simple Example') #标题
plt.ylim(0, 20) #显示的y轴范围
# plt.legend(fontsize=20) #显示图例




# plt.show() #显示作图结果
plt.savefig('resultchange.pdf')
