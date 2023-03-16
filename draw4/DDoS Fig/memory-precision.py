import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

x=['2^8','2^9','2^10','2^11','2^12','2^13','2^14','2^15']

y1=[0.973805855,
0.945402299,
0.998482549,
0.995468278,
1,
1,
0.993975904,
1,
]
y2=[0.990182803,
0.997491377,
0.992548898,
0.983338205,
0.997098085,
0.999126638,
0.993939394,
0.996524761,
]
y3=[0.797800639,
0.876035912,
0.973699764,
0.980938416,
0.980272701,
0.980540227,
0.977726352,
0.978311163,
]




plt.figure(figsize = (10, 9)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y1, color='green',marker='o',linestyle='-',label = 'SYN',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, color='#9370DB',marker='d',linestyle='-',label = 'UDP-C',  linewidth = 2.5)
plt.plot(x, y3, color='#009ACD',marker='s',linestyle='-', label = 'UDP-F', linewidth = 2.5)
# plt.plot(x, y4, color='tomato',marker='^',linestyle='-',label = 'sampling rate=1/64',  linewidth = 2.5)

plt.plot(x, y1, color='green',marker='o',linewidth='2.0',markersize = 12) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, color='#9370DB',marker='d',linewidth='2.0',markersize = 12)
plt.plot(x, y3, color='#009ACD',marker='s',linewidth='2.0',markersize =12)
# plt.plot(x, y4, color='tomato',marker='^',linewidth='2.0',markersize = 12)

ax = plt.subplot(111) #这是画布哦，说明只在一张图显示，也可分割多图
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)

plt.xlabel('w', fontsize=28) # x轴名称
plt.ylabel('Precision (%)', fontsize=24) # y轴名称
# plt.title('A Simple Example') #标题
# plt.ylim(0, 40) #显示的y轴范围
#把x,y轴的刻度间隔设置，并存在变量里
# x_major_locator=MultipleLocator(1)
y_major_locator=MultipleLocator(0.02)
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
plt.savefig('memoryPre.pdf')