import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as mp
from matplotlib.pyplot import MultipleLocator
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

x_lambda = ['1/256','1/512','1/1024','1/2048','1/4096','1/8192'] # x轴
# 左侧y轴：y1_recall
y1_recall = [7.733993749,
8.706879611,
9.532771947,
9.898963421,
10.12890959,
10.21881499
]
# 右侧y轴：y2_preceise
y2_preceise = [66.24473 ,
77.43254 ,
82.72274 ,
85.94673 ,
87.81888 ,
88.78881 ,

]

mp.gcf().set_facecolor(np.ones(3) * 240 / 255)  # 设置背景色
fig, ax1 = plt.subplots()  # 使用subplots()创建窗口
# 绘制折线图像1, 标签，线宽
ax1.plot(x_lambda, y1_recall, c='orangered', label='recall', linewidth=1,marker='o',linestyle='-')
mp.legend(loc=2)
ax2 = ax1.twinx()  # 创建第二个坐标轴
ax2.plot(x_lambda, y2_preceise, c='blue', label='preceise', linewidth=1,marker='d',linestyle='-')  # 同上, 'o-'
mp.legend(loc=4)
plt.grid(True)  # 样式风格：网格型
# ax1.set_title("Double Y axis", size=22)  # 大标题
ax1.set_xlabel('lambda', size=18)
ax1.set_ylabel('Packet rate of DCSS (Mpps)', size=14)
ax2.set_ylabel('Throughput of DSCC (Gbps)', size=14)
# mp.gcf().autofmt_xdate() # 自动适应刻度线密度，包括x轴，y轴
plt.show()

# plt.savefig('DDoS me.pdf')
# plt.savefig('memoryRec.pdf')