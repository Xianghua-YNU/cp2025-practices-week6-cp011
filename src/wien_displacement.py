"""维恩位移定律计算模块

本模块实现了维恩位移定律相关的计算功能，包括：
1. 维恩方程的图像绘制
2. 维恩位移常数的计算
3. 基于维恩位移定律的温度估算

主要函数：
- plot_wien_equation: 绘制维恩方程的图像
- solve_wien_constant: 计算维恩位移常数
- calculate_temperature: 根据波长估算温度
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy import constants

def plot_wien_equation():
    """绘制维恩方程的两个函数图像
    
    绘制方程 5e^(-x) + x - 5 = 0 的图像解释，包括：
    - y = 5e^(-x) 曲线
    - y = 5 - x 直线
    两条曲线的交点即为方程的解
    """
    x = np.linspace(0, 10, 500)  # 在x轴创建一个从0到10之间的500个等间距的数值数组
    # 计算 y = 5e^(-x) 和 y = 5-x
    y1 = 5*np.exp(-x)
    y2 = 5-x
    
    plt.figure(figsize=(8, 6)) # 创建图形并设置大小为8×6英寸
    
    '''
    绘制两条曲线，其中：
    y1 = 5e^(−x)的图例名称为r'$y = 5e^{-x}$'，采用蓝色虚线
    y2 = 5−x的图例名称为r'$y = 5 - x$'，采用红色实线
    '''
    plt.plot(x, y1, label=r'$y = 5e^{-x}$', linestyle='--', color='b')  
    plt.plot(x, y2, label=r'$y = 5 - x$', linestyle='-', color='r')

    # 设置坐标轴标签和标题
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Visualization of Wien’s Displacement Equation')
    plt.legend()  # 添加图例
    plt.grid(True)  # 添加网格
    plt.show()  # 显示图形

def wien_equation(x):
    """维恩方程：5e^(-x) + x - 5 = 0
    
    参数:
    x (float): 方程的自变量
    
    返回:
    float: 方程的函数值
    """
    return 5*np.exp(-x)+x-5

def solve_wien_constant(x0):
    """求解维恩位移常数
    
    通过求解非线性方程 5e^(-x) + x - 5 = 0 得到 x 值，
    然后计算维恩位移常数 b = hc/(k_B * x)
    
    参数:
    x0 (float): 求解方程的初始值
    
    返回:
    tuple: (x, b)
        - x (float): 非线性方程的解
        - b (float): 维恩位移常数，单位：m·K
    """
    
    x = fsolve(wien_equation, x0)[0]
    # 使用fsolve数值方法(找到一个x值，使得wien_equation(x) = 0),求解非线性方程5e^(-x)+x-5=0，其中：
    # wien_equation是已经定义函数，返回5e^(-x)+x-5的值
    # x0是初始猜测值
    # fsolve函数会返回一个数组(只有一个解)，[0]则是对该数组的索引，表示对x赋上数组第一个元素的值
    h = constants.h  # 普朗克常数
    c = constants.c  # 光速
    k_B = constants.k  # 玻尔兹曼常数
    b = (h*c)/(k_B*x)  # 计算维恩位移常数 b = hc/(k_B * x)
    
    return x, b

def calculate_temperature(wavelength, x0=5.0):
    """根据波长计算温度
    
    基于维恩位移定律 λT = b，根据辐射峰值波长计算黑体温度
    
    参数:
    wavelength (float): 峰值波长，单位：米
    x0 (float, optional): 求解方程的初始值，默认为5.0
    
    返回:
    float: 黑体温度，单位：开尔文
    """
    # 计算维恩位移常数
    _, b = solve_wien_constant(x0)
    
    # 计算温度T = b/λ
    temperature = b/wavelength
    return temperature

if __name__ == "__main__":
    # 绘制方程图像
    plot_wien_equation()
    
    # 从键盘输入初值
    try:
        x0 = float(input("请根据图像输入方程求解的初始值（建议值为4-6）："))
    except ValueError:
        print("输入无效，将使用默认值 5")
        x0 = 5
    
    # 计算维恩位移常数
    x, b = solve_wien_constant(x0)
    print(f"\n使用初值 x0 = {x0}")
    print(f"方程的解 x = {x:.6f}")
    print(f"维恩位移常数 b = {b:.6e} m·K")
    
    # 计算太阳表面温度
    wavelength_sun = 502e-9  # 502 nm 转换为米
    temperature_sun = calculate_temperature(wavelength_sun, x0)
    print(f"\n太阳表面温度估计值：{temperature_sun:.0f} K")
