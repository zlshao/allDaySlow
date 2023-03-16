import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']     # 显示中文
# 为了坐标轴负号正常显示。matplotlib默认不支持中文，设置中文字体后，负号会显示异常。需要手动将坐标轴负号设为False才能正常显示负号。
matplotlib.rcParams['axes.unicode_minus'] = False

# #################################拟合优度R^2的计算######################################
def __sst(y_no_fitting):
    """
    计算SST(total sum of squares) 总平方和
    :param y_no_predicted: List[int] or array[int] 待拟合的y
    :return: 总平方和SST
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_no_fitting]
    sst = sum(s_list)
    return sst


def __ssr(y_fitting, y_no_fitting):
    """
    计算SSR(regression sum of squares) 回归平方和
    :param y_fitting: List[int] or array[int]  拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 回归平方和SSR
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_fitting]
    ssr = sum(s_list)
    return ssr


def __sse(y_fitting, y_no_fitting):
    """
    计算SSE(error sum of squares) 残差平方和
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 残差平方和SSE
    """
    s_list = [(y_fitting[i] - y_no_fitting[i])**2 for i in range(len(y_fitting))]
    sse = sum(s_list)
    return sse


def goodness_of_fit(y_fitting, y_no_fitting):
    """
    计算拟合优度R^2
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 拟合优度R^2
    """
    SSR = __ssr(y_fitting, y_no_fitting)
    SST = __sst(y_no_fitting)
    rr = SSR /SST
    return rr



# 定义x、y散点坐标
x = [10000/8,10000/16,10000/32,10000/64,10000/128,15000/8,15000/16,15000/32,15000/64,15000/128,20000/8,20000/16,20000/32,20000/64,20000/128,25000/8,25000/16,25000/32,25000/64,25000/128]
# x = [1/8,1/16,1/32,1/64,1/128]
x = np.array(x)
print('x is :\n', x)
# num = [15,8,4,2,1,23,11,5,2,1,31,15,7,3,1,39,19,9,4,2]
num = [15,8,4,2,1,23,11,5,2,1,31,15,7,3,1,39,19,9,4,2]

# num = [23,11,5,2,1]
y = np.array(num)
print('y is :\n', y)
# 用3次多项式拟合
f1 = np.polyfit(x, y, 1)
print('f1 is :\n', f1)

p1 = np.poly1d(f1)
print('p1 is :\n', p1)

# 也可使用yvals=np.polyval(f1, x)
yvals = p1(x)  # 拟合y值
print('yvals is :\n', yvals)
# 绘图
rr=goodness_of_fit(yvals,y)
print('拟合优度'+str(rr))
plot1 = plt.plot(x, y, 's', label='原始值')
plot2 = plt.plot(x, yvals, 'r', label='拟合曲线')
plt.xlabel('n / p')
plt.ylabel('NoFV ')
plt.legend(loc=4)  # 指定legend的位置右下角
# plt.title('polyfitting')
plt.show()
# plt.savefig('fit.pdf')