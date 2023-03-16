import numpy as np
import pandas as pd
import math
from scipy.stats import norm
import scipy.stats as st
import matplotlib.pyplot as plt #导入Matplotlib
from matplotlib.ticker import MaxNLocator

def get_mean_var_std(arr):
    import numpy as np

    # 求均值
    arr_mean = np.mean(arr)
    # 求方差
    arr_var = np.var(arr)
    # 求标准差
    arr_std = np.std(arr, ddof=1)
    print("平均值为：%f" % arr_mean)
    print("方差为：%f" % arr_var)
    print("标准差为:%f" % arr_std)

    return arr_mean, arr_var, arr_std


if __name__ == '__main__':
    filename='hash_8_bit_Distri.csv'
    df = pd.read_csv(filename,index_col=False)
    print(df['bitC7'])

    # print(get_mean_var_std(arr))
    u =  df['bitC7'].mean()# 均值μ
    sig = df['bitC7'].std()  # 标准差δ
    print("正态性检验：")
    print(st.kstest(df['bitC7'], 'norm'),(u,sig))
    # print(arr)







    # x = np.linspace(u - 3 * sig, u + 3 * sig, 50)  # 定义域
    # y = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)  # 定义曲线函数
    # plt.plot(x, y, "g", linewidth=2)  # 加载曲线
    # plt.grid(True)  # 网格线
    # plt.show()  # 显示
    x = np.arange(0, 150, 0.1)  # 从-5到5 ，步长是 0.1 产生数据
    y = norm.pdf(x, u, sig)
    # x 的意思 大概是 横坐标 ，求出来的y是
    plt.plot(x, y)

    plt.xlabel('x')  # 设置x轴名字
    plt.ylabel('density')  # 设置y轴名字
    plt.show()  # 输出图像

