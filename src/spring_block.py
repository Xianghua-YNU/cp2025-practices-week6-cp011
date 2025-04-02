import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def solve_ode_euler(step_num):
    """
    使用欧拉法求解弹簧 - 质点系统的常微分方程。

    参数:
    step_num (int): 模拟的步数

    返回:
    tuple: 包含时间数组、位置数组和速度数组的元组
    """
    # TODO: 创建存储位置和速度的数组
    position = None
    velocity = None

    # TODO: 计算时间步长
    time_step = None

    # TODO: 设置初始位置和速度
    
    # TODO: 使用欧拉法迭代求解微分方程
    
    # TODO: 生成时间数组
    time_points = None

    return time_points, position, velocity


def spring_mass_ode_func(state, time):
    """
    定义弹簧 - 质点系统的常微分方程。

    参数:
    state (list): 包含位置和速度的列表
    time (float): 时间

    返回:
    list: 包含位置和速度的导数的列表
    """
    # TODO: 从状态中提取位置和速度
    
    # TODO: 计算位置和速度的导数
    
    return [0, 0]  # 替换为正确的返回值


def solve_ode_odeint(step_num):
    """
    使用 odeint 求解弹簧 - 质点系统的常微分方程。

    参数:
    step_num (int): 模拟的步数

    返回:
    tuple: 包含时间数组、位置数组和速度数组的元组
    """
    # TODO: 设置初始条件
    initial_state = None
    
    # TODO: 创建时间点数组
    time_points = None
    
    # TODO: 使用 odeint 求解微分方程
    solution = None
    
    # TODO: 从解中提取位置和速度
    position = None
    velocity = None
    
    return time_points, position, velocity


def plot_ode_solutions(time_euler, position_euler, velocity_euler, time_odeint, position_odeint, velocity_odeint):
    """
    绘制欧拉法和 odeint 求解的位置和速度随时间变化的图像。

    参数:
    time_euler (np.ndarray): 欧拉法的时间数组
    position_euler (np.ndarray): 欧拉法的位置数组
    velocity_euler (np.ndarray): 欧拉法的速度数组
    time_odeint (np.ndarray): odeint 的时间数组
    position_odeint (np.ndarray): odeint 的位置数组
    velocity_odeint (np.ndarray): odeint 的速度数组
    """
    # 创建图形并设置大小
    plt.figure(figsize=(12, 6))
    
    # 绘制位置对比图
    plt.subplot(1, 2, 1)
    plt.plot(time_euler, position_euler, label='Euler Method', linestyle='--')
    plt.plot(time_odeint, position_odeint, label='odeint', linestyle='-')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title('Position vs Time')
    plt.legend()
    plt.grid(True)
    
    # 绘制速度对比图
    plt.subplot(1, 2, 2)
    plt.plot(time_euler, velocity_euler, label='Euler Method', linestyle='--')
    plt.plot(time_odeint, velocity_odeint, label='odeint', linestyle='-')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.title('Velocity vs Time')
    plt.legend()
    plt.grid(True)
    
    # 调整布局并显示图形
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 模拟步数
    step_count = 100
    # TODO: 使用欧拉法求解
    time_euler, position_euler, velocity_euler = solve_ode_euler(step_count)
    # TODO: 使用 odeint 求解
    time_odeint, position_odeint, velocity_odeint = solve_ode_odeint(step_count)
    # TODO: 绘制对比结果
    plot_ode_solutions(time_euler, position_euler, velocity_euler, time_odeint, position_odeint, velocity_odeint)
