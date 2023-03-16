import matplotlib.pyplot as plt #导入Matplotlib
from matplotlib.pyplot import MultipleLocator
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

x  =['1/8','1/16','1/32','1/64','1/128'] #此处也可数字
y1 =[15,8,4,2,1]
y2 =[23,11,5,2,1]
# y3 =[31,15,7,3,1]
y3=[31,16,8,4,2]
y4 =[39,19,9,4,2]

# plt.tick_params(labelsize=23)

plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y1, color='#006D87',marker='o',linestyle='-',label = 'n=10000',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, color='#DD6B4F',marker='d',linestyle='-',label = 'n=15000',  linewidth = 2.5)
plt.plot(x, y3, color='#535164',marker='s',linestyle='-', label = 'n=20000', linewidth = 2.5)
plt.plot(x, y4, color='#FFD700',marker='^',linestyle='-',label = 'n=25000',  linewidth = 2.5)

plt.plot(x, y1, color='#006D87',marker='o',linewidth='2.0',markersize = 10) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, color='#DD6B4F',marker='d',linewidth='2.0',markersize = 10)
plt.plot(x, y3, color='#535164',marker='s',linewidth='2.0',markersize = 10)
plt.plot(x, y4, color='#FFD700',marker='^',linewidth='2.0',markersize = 10)

ax = plt.subplot(111) #这是画布哦，说明只在一张图显示，也可分割多图
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)
y_major_locator=MultipleLocator(3)
ax=plt.gca()
#ax为两条坐标轴的实例
# ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
plt.xlabel('抽样率 ', fontsize=24) # x轴名称
plt.ylabel('特征向量数目 ', fontsize=24) # y轴名称

# plt.xlabel('Sampling Rate ', fontsize=24) # x轴名称
# plt.ylabel('NoFV ', fontsize=24) # y轴名称
# plt.title('A Simple Example') #标题
plt.ylim(0, 40) #显示的y轴范围
plt.grid()
plt.legend(fontsize=20) #显示图例
plt.show()
# plt.savefig('SamplingResult1116.pdf')