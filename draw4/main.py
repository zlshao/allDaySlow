import  matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号


t=np.arange(0.0,2.0,0.1)
s=np.sin(t*np.pi)

plt.figure(figsize=(8,8), dpi=80)
plt.figure(1)
ax1 = plt.subplot(221)
ax1.plot(t,s, color="r",linestyle = "--")
ax2 = plt.subplot(222)
ax2.plot(t,s,color="y",linestyle = "-")
ax3 = plt.subplot(223)
ax3.plot(t,s,color="g",linestyle = "-.")
ax4 = plt.subplot(224)
ax4.plot(t,s,color="b",linestyle = ":")
plt.show()