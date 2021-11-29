# 第十次作业 - YOLO目标检测

<center>姓名：张喆	&emsp;&emsp;&emsp;&emsp;	学号：2101212846	&emsp;&emsp;&emsp;&emsp;	指导老师：张健老师</center>

[toc]

-----

## 问题描述

- 下载运行 YOLOv4( YOLOv5).py代码，测试5幅图 
- 文档中说明跟之前版本的具体改进和不同

## 实验

​	由于之前做过YOLO相关较完善的实验，因此本次作业想回顾并总结之前的YOLO训练自定义数据集的项目。

- [玩具识别](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp)
- [方便面识别](https://github.com/doubleZ0108/Instant-Noodles-Detection)
- [Jetson Nano 使用Yolov3进行目标检测](https://github.com/doubleZ0108/Play-with-NVIDIA-Jetson-Nano/blob/master/experiment/yolov3.md)
- [Jetson Nano使用TensorRT加速yolov3-tiny目标识别](https://github.com/doubleZ0108/Play-with-NVIDIA-Jetson-Nano/blob/master/experiment/trt-yolov3.md)
- [数据集扩充/增强方法和实验](https://github.com/doubleZ0108/Data-Augmentation)

### 实验效果

<img src="https://upload-images.jianshu.io/upload_images/12014150-72e029dfe766cc1d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" style="zoom:50%;" />

<img src="https://upload-images.jianshu.io/upload_images/12014150-674b664e2a3c50b1.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" style="zoom:50%;" />

<img src="https://upload-images.jianshu.io/upload_images/12014150-b7b2dc46a94ed62c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="Untitled-2" style="zoom:80%;" />

<img src="https://upload-images.jianshu.io/upload_images/12014150-ea714025876c2990.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="Untitled" style="zoom:75%;" />

### 数据采集

- 拍摄设备：iPhone 11

- 辅助设备：DJI OSMO Mobile3

<img src="https://upload-images.jianshu.io/upload_images/12014150-e9dc7c5eeef7ca4e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20211129185937500" style="zoom:35%;" />

​	在拍摄的时候尽可能使的画面稳定，iso和曝光大致相同，且不同角度尽可能反映好玩具的不同侧面的样子，因此采用云台的自动跟踪模式进行焦点跟踪

选取了两个场景

- 偏暖色调的沙发
- 偏冷色调的墙壁

​	这两个场景分别与长颈鹿、云与羊颜色相近，也进一步加强目标检测网络的能力

<img src="https://upload-images.jianshu.io/upload_images/12014150-b5cb15286205f88c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200726215112598" width="65%;" />

​	最终筛除掉一些比较劣质的数据，共得到93张有效数据，数量并不是很多，这是因为想通过学习数据集扩充的方法减少人力劳动。

​	同时由于手机像素比较高，每张图片在4M左右，数据量过千之后会训练造成不少的时间消耗，因此在处理之前首先进行[图像压缩预处理](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/util/data_compression.py)，压缩后的图像大概在500k左右。

### 数据增强

<img src="https://upload-images.jianshu.io/upload_images/12014150-f10f6e9648131783.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="20210918215930" style="zoom:40%;" />

​	详细的说明可以参考仓库：https://github.com/doubleZ0108/Data-Augmentation

​	共使用了11种方法进行数据集的扩充

- 图像强度变换
  - 亮度变化： [lightness](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/lightness.py)
  - 对比度变化：[contrast](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/contrast.py)
- 图像滤波
  - 锐化：[sharpen](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/sharpen.py)
  - 高斯模糊：[blur](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/blur.py)
- 透视变换
  - 镜像翻转：[flip](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/flip.py)
  - 图像裁剪：[crop](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/crop.py)
  - 图像拉伸：[deform](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/deform.py)
  - 镜头畸变：[distortion](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/distortion.py)
- 注入噪声
  - 椒盐噪声：[noise](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/noise.py)
  - 渐晕：[vignetting](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/vignetting.py)
- 其他
  - 随机抠除：[cutout](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/cutout.py)

### 数据标注

​	采用[labelImage](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/doc/Study-Notes/labelImg工具.md)工具标注拍到的93张图片，这些图片存放在`main/`目录下，为所有数据中最原始的未处理数据；之后手工标注`_crop`, `_deform`, `_distortion`处理过的数据集，因为这部分如果采用脚本自动生成的话效果会很差，不能达到train集的素质，因此采用手工标注；`_flip`处理过的数据可以通过脚本自动生成有逻辑的标注，其余图像处理也可以直接复制之前手工标注的`main/`中的数据。

<img src="https://upload-images.jianshu.io/upload_images/12014150-3718f965534a4245.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="12014150-279de93f0ef27dcb" style="zoom:20%;" />

**文件命名方法**

`giraffe_10_sharpen.jpg`

- pos0：类别名（people, sheep, giraffe, cloud, two, three, four, etc.)
- pos1: 在此类别中的编号
- pos2: 经过何种图像处理方法

### YOLOv4环境搭建

1. Cloning and Building Darknet

​	clone darknet from AlexeyAB's famous repository,

```bash
git clone https://github.com/AlexeyAB/darknet
```

​	adjust the Makefile to enable OPENCV and GPU for darknet

```bash
cd darknet
sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/GPU=0/GPU=1/' Makefile
sed -i 's/CUDNN=0/CUDNN=1/' Makefile
sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile
```

​	build darknet

```bash
make
```

2. Pre-trained yolov4 weights

​	YOLOv4 has been trained already on the coco dataset which has 80 classes that it can predict. 

```bash
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
```

3. Test env Enabled

```bash
./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights data/person.jpg
```

<img src="https://upload-images.jianshu.io/upload_images/12014150-f1391b4b5f5e86eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20211129164745412" style="zoom:50%;" />

### 训练自定义数据集

- Labeled Custom Dataset
- Custom .cfg file
- obj.data and obj.names files
- train.txt file (test.txt is optional here as well)

1. Gathering and Labeling a Custom Dataset

2. Configuring Files for Training

【cfg file】

​	edit the `yolov4.cfg` to fit the needs based on the object detector

- `bash=64` & `subdivisions=16`：网上比较推荐的参数

- `classes=4` in the three YOLO layers

- `filters=(classes + 5) * 3`: three convolutional layers before the YOLO layers

- `width=416` & `height=416`: any multiple of 32, 416 is standard

  - improve results by making value larger like 608 but will slow down training

- `max_batches=(# of classes) * 2000`: but no less than 6000

- `steps=(80% of max_batches), (90% of max_batches)`

- `random=1`: if run into memory issues or find the training taking a super long time, change three yolo layers from 1 to 0 to speed up training but slightly reduce accurancy of model

【obj.names】

​	one class name per line in the same order as dataset generation step

```names
sheep
giraffe
cloud
snow
```

【obj.data】

```data
classes= 4
train  = data/train.txt
valid  = data/test.txt
names = data/obj.names
backup = backup
```

- `backup`: where save the weights to of the model throughout training

【train.txt and test.txt】

​	hold the reletive paths to all the training images and valididation images, it contain one line for each training image path or validation image path

3. Train Custom Object Detector

​	Download pre-trained weights for the convolutional layers. By using these weights it helps custom object detector to be way more accurate and not have to train as long.

```bash
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137
```

​	train

```bash
./darknet detector train ../../data/obj.data cfg/yolov4_custom.cfg yolov4.conv.137 -dont_show
```

## YOLOv4改进点

​	从YOLOv4开始，YOLO的原作者 **Joseph Redmon**宣布退出CV领域，AlexeyAB接手继续完善并发布了YOLOv4，在性能上较YOLOv4大幅提升。

​	YOLOv4对比了大量当时最新提出的深度学习技巧，例如Swish、Mish激活函数，CutOut和CutMix数据增强方法，DropPath和DropBlock正则化方法，同时主要围绕五大方面进行改进：Mosaic、自对抗训练数据增强方法、修改版本的 SAM 和 PAN、跨Batch的批归一化（BN）。同时权衡了时间和精度使得在一块普通GPU上就能训练的同时能够达到实时性，从而能够在生产环境中部署。

​	作者提到只在训练过程耗时增多但不影响推理耗时又增强模型性能的技巧为bag of freebies；稍微提高推理耗时但显著提升性能的称为bag of specials：

- **bag of freebies**：例如进行数据增强，正则化方法(Drop, DropConnect, DropBlock)，平衡正负样本(Focal loss, OHEM)，改进loss(GIoU, DIoU, CIoU)等
- **bag of specials**：例如增大感受野，注意力机制(Squeeze-and-Excitation(SE), Spatial Attention Module(SAM))，特征融合(FPN, SFAM, BiFPN)，激活函数(LReLU, PReLU)，非最大值抑制后处理(soft-NMS, DIoU NMS)等

​	四张图片拼接为一张图片的Mosaic方法，相当于进一步增加了训练的样本数，同时降低batch数量

<img src="https://upload-images.jianshu.io/upload_images/12014150-f94baf34ddb0f0a2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20211129192157279" style="zoom:50%;" />

​	还有很多其他改进和技巧不再复述，最终的YOLOv4由三部分组成

- CSPDarknet53(backbone)
- SAP + PAN
- YOLOv3

## 参考

[深入浅出Yolo系列之Yolov3&Yolov4&Yolov5&Yolox核心基础知识完整讲解](https://zhuanlan.zhihu.com/p/143747206)

[YOLOv4重磅发布，五大改进，二十多项技巧实验，堪称最强目标检测万花筒](https://zhuanlan.zhihu.com/p/135980432)