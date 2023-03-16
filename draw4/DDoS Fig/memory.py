import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

x=['1/256','1/512','1/1024','1/2048','1/4096','1/8192']
y1=[1.50,0.75,0.75,0.375,0.375,0.1875]
y2=[0.625,0.3125,0.3125,0.15625,0.15625,0.078125]
y3=[2.12500 ,1.06250 ,1.06250 ,0.53125,0.53125,0.26563]




plt.figure(figsize = (10, 9)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y1, color='green',marker='o',linestyle='-',label = 'Me of TCP sketch',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, color='#9370DB',marker='d',linestyle='-',label = 'Me of UDP sketch',  linewidth = 2.5)
plt.plot(x, y3, color='#009ACD',marker='s',linestyle='-', label = 'Me of DCSS', linewidth = 2.5)
# plt.plot(x, y4, color='tomato',marker='^',linestyle='-',label = 'sampling rate=1/64',  linewidth = 2.5)

plt.plot(x, y1, color='green',marker='o',linewidth='2.0',markersize = 12) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, color='#9370DB',marker='d',linewidth='2.0',markersize = 12)
plt.plot(x, y3, color='#009ACD',marker='s',linewidth='2.0',markersize =12)
# plt.plot(x, y4, color='tomato',marker='^',linewidth='2.0',markersize = 12)

ax = plt.subplot(111) #这是画布哦，说明只在一张图显示，也可分割多图
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)

plt.xlabel('Sampling rate ', fontsize=24) # x轴名称
plt.ylabel('Memory(MB)', fontsize=24) # y轴名称
# plt.title('A Simple Example') #标题
# plt.ylim(0, 40) #显示的y轴范围
#把x,y轴的刻度间隔设置，并存在变量里
# x_major_locator=MultipleLocator(1)
y_major_locator=MultipleLocator(0.2)
ax=plt.gca()
#ax为两条坐标轴的实例
# ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为10的倍数
# plt.ylim(-5,90)


plt.grid()
plt.legend(fontsize=20) #显示图例
# plt.show()
plt.savefig('DDoS me.pdf')