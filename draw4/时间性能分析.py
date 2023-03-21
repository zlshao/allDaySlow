import matplotlib.pyplot as plt #导入Matplotlib
from matplotlib.pyplot import MultipleLocator
import seaborn as sns
import matplotlib.gridspec as gridspec
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

x  =['1','1/8','1/16','1/32'] #此处也可数字
resultFig='结果pdf/时间性能.pdf'
plt.figure(figsize=(15,16))
gs = gridspec.GridSpec(3, 6) # 创立2 * 6 网格
# gs.update(wspace=0.8)
y11=[8122.1,
1032.3,
532.5,
267.8]


y21 =[38.275908,
4.7692674,
2.324751199,
1.173915]


y31 =[11.9894562,
1.393952700,
0.7213980,
0.38083560]


y41 =[4.8612039,
2.50636250,
1.44460169,
0.68956369]

y51=[8177.2265681,
1040.9695826,
536.990750889,
270.04431429]


ax1 = plt.subplot(gs[0, :3]) # gs(哪一行，绘制网格列的范围)
plt.ylim(0, 8700) #显示的y轴范围
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.bar(x,y11, color='#203378',width=0.6)
for a,b in zip(x,y11):   #柱子上的数字显示
 plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=18);
plt.xticks(fontsize=20)#嗯调调字体
plt.yticks(fontsize=20)
y_major_locator2=MultipleLocator(1600)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator2)
plt.xlabel('(a) Sketch处理时间(s) ', fontsize=20) # x轴名称
# plt.grid()
# plt.legend(fontsize=20) #显示图例



ax2 = plt.subplot(gs[0, 3:])
plt.ylim(0, 42) #显示的y轴范围
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.bar(x,y21, color='#6989b9',width=0.6)
for a,b in zip(x,y21):   #柱子上的数字显示
 plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=18);
plt.xticks(fontsize=20)#嗯调调字体
plt.yticks(fontsize=20)
y_major_locator2=MultipleLocator(5)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator2)
plt.xlabel('(b) 检测时间(s) ', fontsize=20) # x轴名称
# plt.grid()
# plt.legend(fontsize=20) #显示图例

ax3 = plt.subplot(gs[1, :3])
plt.ylim(0, 13) #显示的y轴范围
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.bar(x,y31, color='#a9c1a3',width=0.6)
for a,b in zip(x,y31):   #柱子上的数字显示
 plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=18);
plt.xticks(fontsize=20)#嗯调调字体
plt.yticks(fontsize=20)
y_major_locator2=MultipleLocator(2)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator2)
plt.xlabel('(c) 过滤并输出扫描器IP时间(s) ', fontsize=20) # x轴名称
# plt.grid()
# plt.legend(fontsize=20) #显示图例

ax4 = plt.subplot(gs[1, 3:])
plt.ylim(0, 5.5) #显示的y轴范围
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.bar(x,y41, color='#e3bf2b',width=0.6)
for a,b in zip(x,y41):   #柱子上的数字显示
 plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=18);
plt.xticks(fontsize=20)#嗯调调字体
plt.yticks(fontsize=20)
y_major_locator2=MultipleLocator(1)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator2)
plt.xlabel('(d) 聚类时间(s) ', fontsize=20) # x轴名称
# plt.grid()
# plt.legend(fontsize=20) #显示图例


ax5 = plt.subplot(gs[2, 1:5])
plt.ylim(0, 8700) #显示的y轴范围
# plt.figure(figsize = (10, 10)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.bar(x,y51, color='#edea9b',width=0.5)
for a,b in zip(x,y51):   #柱子上的数字显示
 plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=18);
plt.xticks(fontsize=20)#嗯调调字体
plt.yticks(fontsize=20)
y_major_locator2=MultipleLocator(1600)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator2)
plt.xlabel('(e) 总时间(s) ', fontsize=20) # x轴名称
# plt.grid()




plt.show()
# plt.savefig(resultFig)