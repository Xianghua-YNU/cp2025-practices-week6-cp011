import numpy as np
import matplotlib.pyplot as plt

def setup_parameters():
    """
    设置模拟牛顿环所需的参数
    
    返回:
    tuple: 包含激光波长(lambda_light,单位m)、透镜曲率半径(R_lens,单位m)的元组
    """
    # 氦氖激光波长 (m)
    lambda_light = 632.8e-9
    # 透镜曲率半径 (m)
    R_lens = 0.1
    return lambda_light, R_lens

def generate_grid():
    """
    生成模拟所需的网格坐标
    
    返回:
    tuple: 包含网格坐标X、Y以及径向距离r的元组
    """
    # 创建一个以(0,0)为中心的二维网格，并计算了每个点到中心的距离r
    # 用于在牛顿环模拟中用于计算光程差和干涉条纹的分布。
    x = np.linspace(-1e-3, 1e-3, 1000) # 在-1mm到1mm范围内生成1000个均匀分布的数，赋值给x，形成一个列表
    y = np.linspace(-1e-3, 1e-3, 1000) # 逻辑同上
    X, Y = np.meshgrid(x, y)  # 生成二维坐标网格，其中：
                              # X表示所有网格点的x坐标，是一个大小1000×1000的矩阵
                              # Y表示所有网格点的y坐标，是一个大小1000×1000的矩阵
    r = np.sqrt(X**2 + Y**2)  # 计算每个网格点到坐标原点(0,0)的径向距离r
    return X, Y, r

def calculate_intensity(r, lambda_light, R_lens):
    """
    计算干涉强度分布
    
    参数:
    r (np.ndarray): 径向距离数组
    lambda_light (float): 激光波长(m)
    R_lens (float): 透镜曲率半径(m)
    
    返回:
    np.ndarray: 干涉强度分布数组
    """
    # 在此实现光强计算
    d = (r**2)/(2*R_lens)                 # d=r^2/(2*R_lens)
    phase = (2*np.pi/lambda_light)*(2*d)  # 相位差phase=(2π/lambda_light)*2d(光反射两次的光程差)
    intensity = (1+np.cos(phase))/2       # 光强干涉公式I/I0=(1+cos(phase))/2
    return intensity

def plot_newton_rings(intensity):
    """
    绘制牛顿环干涉条纹图像
    
    参数:
    intensity (np.ndarray): 干涉强度分布数组
    """
    # 在此实现图像绘制
    plt.figure(figsize=(6,6))  # 创建一个6×6英寸的图像窗口
    plt.imshow(intensity, cmap='gray', extent=(-1, 1, -1, 1))
    # 显示光强的二维图像，颜色映射设置为灰度模式，x坐标轴的范围从-1mm到1mm，y坐标轴的范围从-1mm到1mm
    plt.colorbar(label='Intensity')  # 给颜色条添加标签 “Intensity”
    plt.title("Newton's Rings Interference Pattern")  #设置图像标题
    plt.xlabel("x (mm)")  # 设置x轴和y轴的标签分别为x (mm)、y (mm)
    plt.ylabel("y (mm)")
    plt.show()  # 显示图像

if __name__ == "__main__":
    # 1. 设置参数
    lambda_light, R_lens = setup_parameters()
    
    # 2. 生成网格坐标
    X, Y, r = generate_grid()
    
    # 3. 计算干涉强度分布
    intensity = calculate_intensity(r, lambda_light, R_lens)
    
    # 4. 绘制牛顿环
    plot_newton_rings(intensity)
