import os
import cv2
import numpy as np
import pandas as pd
import math
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib.pyplot as plt
import matplotlib as mpl

# 创建图表文件夹
if not os.path.exists('图表'):
    os.mkdir('图表')
    print('创建空文件夹 图表')

# 设置中文字体（使用系统已有的字体）
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'SimHei', 'DejaVu Sans']
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 绘图
plt.plot([1,2,3], [100,500,300])
plt.title('matplotlib 中文字体测试', fontsize=25)
plt.xlabel('X轴', fontsize=15)
plt.ylabel('Y轴', fontsize=15)
plt.show()  # 弹出窗口显示图像