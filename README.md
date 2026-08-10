# OpenCV 计算机视觉练习项目

这是一个以 Python 和 OpenCV 为主的计算机视觉学习与实践仓库，内容从图像/视频读写、颜色空间、鼠标与滑动条交互等基础操作，逐步扩展到滤波、边缘检测、二值化、形态学、轮廓提取、装甲板灯条检测，以及 Labelme 数据处理和 YOLOv8 三角形关键点检测。

仓库同时包含示例图片、测试视频、关键点数据集和已训练权重，适合按脚本编号循序练习，也可以作为 OpenCV 与 YOLOv8 视觉任务的参考代码。

## 主要内容

| 文件或目录 | 内容 |
| --- | --- |
| `1_*.py` | OpenCV 窗口、图像读写、摄像头与视频、鼠标事件、Trackbar |
| `2_*.py` | 颜色空间、NumPy 数组、OpenCV Mat/通道操作 |
| `3_1_drawshape.py` | 使用鼠标绘制直线、矩形和圆形 |
| `6_*.py` | 常见滤波、Sobel/Scharr/Laplacian、Canny 边缘检测 |
| `7_*.py` | 固定/自适应阈值、腐蚀膨胀与形态学操作 |
| `8_1_counters.py` | 轮廓查找与绘制 |
| `Identification_plate*.py` | 基于背景建模或 HSV 颜色阈值的运动目标/装甲板灯条检测 |
| `9_*.py` | Labelme 标注检查、数据可视化、训练/验证集划分、YOLO 格式转换 |
| `10_1_YOLOV8.py` | 调用摄像头进行 YOLOv8 关键点实时推理 |
| `10_2_.py` | YOLOv8 关键点结果自定义绘制与视频逐帧处理 |
| `Triangle_215.yaml` | 三角形关键点数据集配置 |
| `datasets/` | 三角形关键点训练/验证图片及 YOLO 标注 |
| `runs/pose/` | YOLOv8 Pose 训练输出与权重 |

## 环境要求

- Python 3.9 或更高版本
- 支持图形界面的本地运行环境（多数示例使用 `cv2.imshow`）
- 摄像头（运行实时采集或推理示例时需要）
- NVIDIA GPU 与 CUDA 为可选项；YOLOv8 在没有 GPU 时会使用 CPU

创建虚拟环境：

```bash
python -m venv .venv
```

Windows：

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS：

```bash
source .venv/bin/activate
```

安装基础示例依赖：

```bash
pip install opencv-python numpy
```

安装数据处理和 YOLOv8 相关依赖：

```bash
pip install pandas tqdm matplotlib labelme ultralytics torch
```

`Identification_plate1.0.0.py` 使用了 `cv2.bgsegm`。如需运行该脚本，请使用带扩展模块的 OpenCV 包，并避免在同一环境中同时安装多个 OpenCV wheel：

```bash
pip uninstall -y opencv-python opencv-contrib-python
pip install opencv-contrib-python
```

## 快速开始

克隆仓库并进入目录：

```bash
git clone https://github.com/CDC666-666/Opencv.git
cd Opencv
```

运行一个不依赖外部图片的窗口示例：

```bash
python 1_1_show.py
```

运行摄像头采集示例：

```bash
python 1_4_videocapture.py
```

运行 Canny 边缘检测示例：

```bash
python 6_3_canny.py
```

运行装甲板灯条检测：

```bash
python Identification_plate1.0.1.py
```

多数交互式脚本使用以下按键：

- `q`：退出窗口或视频循环
- `s`：在图像保存示例中保存当前图片

## 运行前修改资源路径

部分脚本保留了作者本机的 Linux 绝对路径，例如：

```python
img = cv2.imread('/home/c/桌面/Opencv/test_1.jpg')
video_path = '/home/c/桌面/Opencv/video.avi'
```

运行前请把它们修改为你本机的实际路径。若资源位于仓库根目录，推荐使用相对路径：

```python
img = cv2.imread('test_1.jpg')
video_path = 'video.avi'
```

摄像头示例默认使用 `cv2.VideoCapture(0)`。如果系统有多个摄像头，可尝试将索引改为 `1`、`2` 等。

## Labelme 与数据集处理

仓库中的数据处理脚本可以组成以下流程：

1. 使用 Labelme 对图片进行框和关键点标注。
2. 使用 `9_1_labelme.py` 读取标注并生成汇总数据。
3. 使用 `9_2_DataVisualization.py` 检查数据分布和标注可视化结果。
4. 使用 `9_3_Dividefiles .py` 划分训练集与验证集。
5. 使用 `9_4_Labelme2YOLO.py` 将 Labelme JSON 转换为 YOLO 标注。
6. 检查 `Triangle_215.yaml` 中的数据集根目录、类别和关键点配置。

这些脚本中的 `Dataset_root` 当前指向作者本机目录，且部分脚本使用的是不同示例数据集名称。执行前请统一修改为你的数据集目录。数据集的典型结构如下：

```text
datasets/Triangle_215_Keypoint_YOLO/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

`Triangle_215.yaml` 当前配置了 1 个目标类别 `sjb_rect` 和 3 个关键点，每个关键点包含 `x`、`y`、`visibility` 三个值。Linux 路径区分大小写，请确认 YAML 中的目录名与仓库中的 `Triangle_215_Keypoint_YOLO` 完全一致。

## YOLOv8 关键点训练与推理

使用 Ultralytics CLI 启动训练的示例：

```bash
yolo pose train model=yolov8n-pose.pt data=Triangle_215.yaml imgsz=640 epochs=100 name=Triangle_215
```

训练完成后，将脚本中的模型路径改为实际生成的 `best.pt` 路径。仓库当前推理脚本使用：

```python
model = YOLO('./runs/pose/Triangle_215/n_pretrain/weights/best.pt')
```

启动摄像头实时关键点推理：

```bash
python 10_1_YOLOV8.py
```

处理本地视频并自定义绘制关键点：

```bash
python 10_2_.py
```

运行 `10_2_.py` 前，请修改文件底部 `generate_video(...)` 的输入路径以及函数中的输出路径；当前代码中的路径是作者本机示例路径。

## 常见问题

### `cv2.imread` 返回 `None`

通常是图片路径错误。确认文件存在，并优先改用相对于仓库根目录的路径。

### 摄像头无法读取画面

检查摄像头权限和设备索引，关闭正在占用摄像头的其他软件，再尝试更换 `VideoCapture` 的索引。

### 提示 `module 'cv2' has no attribute 'bgsegm'`

该模块属于 OpenCV contrib，请按照上方说明安装 `opencv-contrib-python`。

### YOLOv8 提示找不到权重或数据集

检查脚本中的 `best.pt` 路径和 `Triangle_215.yaml` 中的 `path`。相对路径以当前终端所在目录为基准。

### 远程服务器运行时无法显示窗口

`cv2.imshow` 需要桌面图形环境。无图形界面时，可将结果改为使用 `cv2.imwrite` 或 `VideoWriter` 保存到文件。

## 说明

本仓库目前未提供开源许可证。在许可证补充之前，代码的复制、修改和再发布权利默认保留给仓库作者。

