# 说明
# 采样数据为单列excel文件，输出为频域图

# 安装依赖
# pip install pandas numpy matplotlib openpyxl

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取Excel文件
file_path = 'your_excel_file.xlsx'  # 请将此替换为您的Excel文件路径
data = pd.read_excel(file_path, engine='openpyxl', header=None)
sample_interval = 0.000001  # 单位为s
# 提取数据
time_series = data[0].values

# 执行傅里叶变换
fft_result = np.fft.fft(time_series)

# 计算频率
n = len(time_series)
frequencies = np.fft.fftfreq(n, sample_interval)

# 绘制频谱图
plt.plot(frequencies, np.abs(fft_result))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')
plt.show()
