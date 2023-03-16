import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

x=['4','8','16','32','64','128','256']
y1=[0.2279,0.1104,0.0314,0.0057,0.0007,0.0001,0.0000]
y2=[0.3163,0.1267,0.0306,0.0048,0.0005,0.0000,0.0000]
y3=[0.4006,0.1318,0.0277,0.0039,0.0004,0.0000,0.0000]
y4=[0.4891,0.1370,0.0243,0.0031,0.0003,0.0000,0.0000]



plt.figure(figsize = (10, 9)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y1, color='#006D87',marker='o',linestyle='-',label = '抽样率=1/8',  linewidth = 2) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, color='#DD6B4F',marker='d',linestyle='-',label = '抽样率=1/16',  linewidth = 2)
plt.plot(x, y3, color='#535164',marker='s',linestyle='-', label = '抽样率=1/32', linewidth = 2)
plt.plot(x, y4, color='#FFD700',marker='^',linestyle='-',label = '抽样率=1/64',  linewidth = 2)

plt.plot(x, y1, color='#006D87',marker='o',linewidth='2.0',markersize = 10) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, color='#DD6B4F',marker='d',linewidth='2.0',markersize = 10)
plt.plot(x, y3, color='#535164',marker='s',linewidth='2.0',markersize =10)
plt.plot(x, y4, color='#FFD700',marker='^',linewidth='2.0',markersize = 10)

ax = plt.subplot(111) #这是画布哦，说明只在一张图显示，也可分割多图
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)

plt.xlabel('内存大小(MB) ', fontsize=24) # x轴名称
plt.ylabel('相对误差(%)', fontsize=24) # y轴名称
# plt.title('A Simple Example') #标题
# plt.ylim(0, 40) #显示的y轴范围
#把x,y轴的刻度间隔设置，并存在变量里
# x_major_locator=MultipleLocator(1)
y_major_locator=MultipleLocator(0.04)
ax=plt.gca()
#ax为两条坐标轴的实例
# ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为10的倍数
# plt.ylim(-5,90)


plt.grid()
plt.legend(fontsize=20) #显示图例
plt.show()
# plt.savefig('RE1115.pdf')