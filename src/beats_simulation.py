import numpy as np
import matplotlib.pyplot as plt

def simulate_beat_frequency(f1=440, f2=444, A1=1.0, A2=1.0, t_start=0, t_end=1, num_points=5000, show_plot=True):
    """
    任务1: 拍频现象的数值模拟
    参数说明:
        f1, f2: 两个波的频率(Hz)
        A1, A2: 两个波的振幅
        t_start, t_end: 时间范围(s)
        num_points: 采样点数
    """
    # 学生任务1: 生成时间范围
    t = np.linspace(t_start, t_end, num_points)
    
    # 学生任务2: 生成两个正弦波
    wave1 = A1 * np.sin(2 * np.pi * f1 * t)
    wave2 = A2 * np.sin(2 * np.pi * f2 * t)

    # 学生任务3: 叠加两个波
    superposed_wave = wave1 + wave2

    # 学生任务4: 计算拍频
    beat_frequency = abs(f1 - f2)

    # 学生任务5: 绘制图像
    if show_plot:
        plt.figure(figsize=(12, 6))
        
        # 绘制第一个波
        plt.subplot(3, 1, 1)
        # 学生任务6: 完成wave1的绘制
        plt.plot(t, wave1, label=f'{f1} Hz')
        plt.plot(t, superposed_wave, label=f'Beat frequency {beat_frequency} Hz', linestyle='--')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Waveforms and Beat Frequency')
        plt.legend()
        plt.grid(True)
        plt.show()
        # 绘制第二个波
        plt.subplot(3, 1, 2)
        # 学生任务7: 完成wave2的绘制
        plt.plot(t, wave2, label=f'{f2} Hz')
        plt.plot(t, superposed_wave, label=f'Beat frequency {beat_frequency} Hz', linestyle='--')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Waveforms and Beat Frequency')
        plt.legend()
        plt.grid(True)
        plt.show()
        # 绘制叠加波
        plt.subplot(3, 1, 3)
        # 学生任务8: 完成superposed_wave的绘制

        plt.tight_layout()
        plt.show()

    return t, superposed_wave, beat_frequency

def parameter_sensitivity_analysis():
    """
    任务2: 参数敏感性分析
    需要完成:
    1. 分析不同频率差对拍频的影响
    2. 分析不同振幅比例对拍频的影响
    """
    # 学生任务9: 频率差分析
    plt.figure(1, figsize=(12, 8))
    # 学生需要在此处添加频率差分析的代码
    delta_f_values = [1, 2, 5, 10]
    for delta_f in delta_f_values:
        f2 = 440 + delta_f
        t, wave, beat_freq = simulate_beat_frequency(440, f2, 1.0, 1.0, show_plot=False)
        plt.plot(t, wave, label=f'Delta f = {delta_f} Hz')
        
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Effect of Frequency Difference on Beat Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()
    # 学生任务10: 振幅比例分析
    plt.figure(2, figsize=(12, 8))
    # 学生需要在此处添加振幅比例分析的代码
    A2_values = [0.5, 1.0, 2.0, 5.0]
    for A2 in A2_values:
        t, wave, beat_freq = simulate_beat_frequency(440, 444, 1.0, A2, show_plot=False)
        plt.plot(t, wave, label=f'A2/A1 = {A2}')

    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Effect of Amplitude Ratio on Beat Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    # 示例调用
    print("=== 任务1: 基本拍频模拟 ===")
    t, wave, beat_freq = simulate_beat_frequency()
    print(f"计算得到的拍频为: {beat_freq} Hz")
    
    print("\n=== 任务2: 参数敏感性分析 ===")
    parameter_sensitivity_analysis()
