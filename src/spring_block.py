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
    # 创建存储位置和速度的数组，长度为 step_num + 1
    position = np.zeros(step_num + 1)
    velocity = np.zeros(step_num + 1)

    # 计算时间步长，假设总时间周期为 2π
    time_step = 2 * np.pi / step_num

    # 设置初始位置和速度
    position[0] = 0  # 初始位置
    velocity[0] = 1  # 初始速度

    # 使用欧拉法迭代求解微分方程
    for i in range(step_num):
        # 根据当前速度更新位置
        position[i + 1] = position[i] + velocity[i] * time_step
        # 根据微分方程 dv/dt = -x 更新速度（假设 k/m = 1）
        velocity[i + 1] = velocity[i] - position[i] * time_step

    # 生成时间数组
    time_points = np.arange(step_num + 1) * time_step

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
    position, velocity = state
    d_position_dt = velocity  # 位置的导数是速度
    d_velocity_dt = -position  # 速度的导数是加速度（由 F = -kx 确定）
    return [d_position_dt, d_velocity_dt]


def solve_ode_odeint(step_num):
    """
    使用 odeint 求解弹簧 - 质点系统的常微分方程。

    参数:
    step_num (int): 模拟的步数

    返回:
    tuple: 包含时间数组、位置数组和速度数组的元组
    """
    # 初始条件，位置 = 0，速度 = 1
    initial_state = [0, 1]
    # 生成时间点数组，均匀分布在 0 到 2π 之间
    time_points = np.linspace(0, 2 * np.pi, step_num + 1)
    # 使用 odeint 数值求解微分方程
    solution = odeint(spring_mass_ode_func, initial_state, time_points)
    # 提取位置和速度数据
    position = solution[:, 0]
    velocity = solution[:, 1]
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
    plt.figure(figsize=(12, 6))

    # 绘制位置对比图
    plt.subplot(1, 2, 1)
    plt.plot(time_euler, position_euler, 'ro', label='Euler Position')  # 欧拉法位置
    plt.plot(time_odeint, position_odeint, 'b-', label='ODEint Position')  # odeint 位置
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title('Position Comparison')
    plt.legend()
    plt.grid(True)

    # 绘制速度对比图
    plt.subplot(1, 2, 2)  # 创建一个1行2列的子图，并选择第2个子图
    plt.plot(time_euler, velocity_euler, 'gs', label='Euler Velocity')  # 用绿色方块(gs)标记欧拉法计算的速度
    plt.plot(time_odeint, velocity_odeint, 'm-', label='ODEint Velocity')  # 用洋红色实线(m-)绘制odeint计算的速度
    plt.xlabel('Time')  # 设置x轴标签为"Time"，y轴标签为 "Velocity"
    plt.ylabel('Velocity')  
    plt.title('Velocity Comparison')  # 设置图表标题为"Velocity Comparison"
    plt.legend()  # 显示图例
    plt.grid(True)  # 显示网格
    plt.tight_layout()  # 调整子图布局，防止重叠
    plt.show()  # 显示绘制的图像


if __name__ == "__main__":
    step_count = 100  # 设置模拟步数
    time_euler, position_euler, velocity_euler = solve_ode_euler(step_count)  # 使用欧拉法求解微分方程
    time_odeint, position_odeint, velocity_odeint = solve_ode_odeint(step_count)  # 使用 odeint 求解微分方程
    # 绘制两种方法的解并进行比较
    plot_ode_solutions(time_euler, position_euler, velocity_euler, time_odeint, position_odeint, velocity_odeint)

