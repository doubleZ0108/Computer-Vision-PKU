# 第七次作业 - 图像超分辨率

<center>姓名：张喆	&emsp;&emsp;&emsp;&emsp;	学号：2101212846	&emsp;&emsp;&emsp;&emsp;	指导老师：张健老师</center>

[toc]

-----

## 问题描述

Github或者主页下载运行一个超分算法，获得结果试着训练一两个Epoch，给出超分结果

## 算法简介

在本次作业中选取基于深度学习超分的经典算法SRCNN进行实验 ([论文](https://arxiv.org/pdf/1501.00092.pdf) | [代码](https://github.com/yjn870/SRCNN-pytorch))

SRCNN作为基于深度学习进行图像超分的开山之作，网络结构比较简单，如下所示：

![](https://pic3.zhimg.com/80/v2-dd756ced7917c139b0770a6971bc62be_1440w.jpg)

首先使用双三次插值将第分辨率图像放大成目标尺寸，接着通过三层卷积网络充当非线性函数映射，最终输出高分辨率图像，网络结构PyTorch版本实现如下：

```python
self.conv1 = nn.Conv2d(num_channels, 64, kernel_size=9, padding=9 // 2)
self.conv2 = nn.Conv2d(64, 32, kernel_size=5, padding=5 // 2)
self.conv3 = nn.Conv2d(32, num_channels, kernel_size=5, padding=5 // 2)
self.relu = nn.ReLU(inplace=True)
```

## 代码模块分析

**文件**主要分为以下几个部分：

- 数据集
  - `data`: 测试数据
  - `train`: 训练数据(`.h5`格式)
  - `eval`: 验证数据集
- 模型
  - `output`: 自己创建用于保存模型输出
  - `weights`: 预训练模型

**代码部分**主要分为以下几个部分：

- `train.py`: 整体训练过程文件，核心包括参数读取，模型、loss、优化器定义，数据集载入，每个epoch训练和验证等
- `test.py`: 针对一张测试图片，对其降采样，并通过bicubic和SRCNN进行超分，输出结果
- `models.py`: 定义SRCNN整体网络结构
- `datasets.py`: 训练和测试数据集数据结构，主要用在DataLoader中以batch为单位进行处理中
- `prepare.py`: 构建自定义数据集

## 环境搭建及实验

**实验环境**：

- 操作系统：Ubnutu 18.04
- 语言：Python 3.7
- 深度学习框架: PyTorch 1.9.1

**训练完所有epoch的截图**：

![image.png](https://upload-images.jianshu.io/upload_images/12014150-b7e97cd08f84c399.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**使用官方数据集进行测试**：

![image.png](https://upload-images.jianshu.io/upload_images/12014150-9db34cdc34888a5a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/12014150-f2a40bc8ebd4c10f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**使用自己采集的数据进行测试**：

![image.png](https://upload-images.jianshu.io/upload_images/12014150-c56b2491c4224e8e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/12014150-9ed91aa1b4d58c3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)