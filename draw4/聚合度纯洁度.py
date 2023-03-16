import matplotlib.pyplot as plt #导入Matplotlib
from matplotlib.pyplot import MultipleLocator
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

x  =['1','1/8','1/16','1/32'] #此处也可数字
resultFig='结果pdf/6子图.pdf'
plt.figure(figsize=(20,24))

plt.subplot(321)
# sns.stripplot(x="onset_days",y="leader_1st",data=data_t,hue="sample_type") # 使用seaborn画图
plt.ylim(0, 1.05) #显示的y轴范围

y11=[1.0,1.0,1.0,0.6]
y12=[0.38,0.83,0.83,0.75]

y21 =[1.0,1.0,1.0,1.0]
y22 =[1.0,1.0,1.0,1.0]

y31 =[1.0,1.0,1.0,0.8]
y32 =[1.0,1.0,1.0,1.0]

y41 =[1.0,1.0,1.0,0.4]
y42 =[1.0,1.0,1.0,1.0]

y51 =[1.0,1.0,1.0,1.0]
y52 =[1.0,1.0,1.0,1.0]

y61 =[1.0,1.0,1.0,1.0]
y62 =[1.0,1.0,1.0,1.0]


# y3 =[31,15,7,3,1]
# y3=[31,16,8,4,2]
# y4 =[39,19,9,4,2]

# plt.tick_params(labelsize=23)
plt.subplot(321)
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y11, color='#006D87',marker='o',linestyle='-',label = '聚合度',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y12, color='#DD6B4F',marker='d',linestyle='-',label = '纯净度',  linewidth = 2.5)
plt.plot(x, y11, color='#006D87',marker='o',linewidth='2.5',markersize = 12) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y12, color='#DD6B4F',marker='d',linewidth='2.5',markersize = 12)
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)
y_major_locator=MultipleLocator(0.1)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
plt.grid()
plt.legend(fontsize=20) #显示图例
plt.xlabel('（a）分布式TCP水平扫描 ', fontsize=24) # x轴名称



plt.subplot(322)
plt.ylim(0, 1.05) #显示的y轴范围
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y21, color='#006D87',marker='o',linestyle='-',label = '聚合度',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y22, color='#DD6B4F',marker='d',linestyle='-',label = '纯净度',  linewidth = 2.5)
plt.plot(x, y21, color='#006D87',marker='o',linewidth='2.5',markersize = 12) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y22, color='#DD6B4F',marker='d',linewidth='2.5',markersize = 12)
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)
y_major_locator2=MultipleLocator(0.1)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator2)
plt.xlabel('（b）分布式TCP垂直扫描 ', fontsize=24) # x轴名称
plt.grid()
plt.legend(fontsize=20) #显示图例

plt.subplot(323)
plt.ylim(0, 1.05) #显示的y轴范围
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y31, color='#006D87',marker='o',linestyle='-',label = '聚合度',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y32, color='#DD6B4F',marker='d',linestyle='-',label = '纯净度',  linewidth = 2.5)
plt.plot(x, y31, color='#006D87',marker='o',linewidth='2.5',markersize = 12) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y32, color='#DD6B4F',marker='d',linewidth='2.5',markersize = 12)
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)
y_major_locator2=MultipleLocator(0.1)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator2)
plt.xlabel('（c）分布式TCP混合扫描 ', fontsize=24) # x轴名称
plt.grid()
plt.legend(fontsize=20) #显示图例

plt.subplot(324)
plt.ylim(0, 1.05) #显示的y轴范围
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y41, color='#006D87',marker='o',linestyle='-',label = '聚合度',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y42, color='#DD6B4F',marker='d',linestyle='-',label = '纯净度',  linewidth = 2.5)
plt.plot(x, y41, color='#006D87',marker='o',linewidth='2.5',markersize = 12) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y42, color='#DD6B4F',marker='d',linewidth='2.5',markersize = 12)
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)
y_major_locator2=MultipleLocator(0.1)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator2)
plt.xlabel('（d）分布式UDP水平扫描 ', fontsize=24) # x轴名称
plt.grid()
plt.legend(fontsize=20) #显示图例

plt.subplot(325)
plt.ylim(0, 1.05) #显示的y轴范围
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y51, color='#006D87',marker='o',linestyle='-',label = '聚合度',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y52, color='#DD6B4F',marker='d',linestyle='-',label = '纯净度',  linewidth = 2.5)
plt.plot(x, y51, color='#006D87',marker='o',linewidth='2.5',markersize = 12) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y52, color='#DD6B4F',marker='d',linewidth='2.5',markersize = 12)
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)
y_major_locator2=MultipleLocator(0.1)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator2)
plt.xlabel('（e）分布式UDP垂直扫描 ', fontsize=24) # x轴名称
plt.grid()
plt.legend(fontsize=20) #显示图例

plt.subplot(326)
plt.ylim(0, 1.05) #显示的y轴范围
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y61, color='#006D87',marker='o',linestyle='-',label = '聚合度',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y62, color='#DD6B4F',marker='d',linestyle='-',label = '纯净度',  linewidth = 2.5)
plt.plot(x, y61, color='#006D87',marker='o',linewidth='2.5',markersize = 12) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y62, color='#DD6B4F',marker='d',linewidth='2.5',markersize = 12)
plt.xticks(fontsize=24)#嗯调调字体
plt.yticks(fontsize=24)
y_major_locator2=MultipleLocator(0.1)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator2)
plt.xlabel('（f）分布式UDP混合扫描 ', fontsize=24) # x轴名称
plt.grid()
plt.legend(fontsize=20) #显示图例


plt.show()
# plt.savefig(resultFig)