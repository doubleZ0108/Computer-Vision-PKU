# 第九次作业 - 风格迁移

<center>姓名：张喆	&emsp;&emsp;&emsp;&emsp;	学号：2101212846	&emsp;&emsp;&emsp;&emsp;	指导老师：张健老师</center>

[toc]

-----

## 问题描述

- 寻找一篇2020/2021年风格迁移的文章
- 翻译其摘要和贡献；对代码主体部分进行注释，截图
- 配置环境，测试自己的图片进行风格迁移的结果，截图

## 论文阅读

AdaAttN: Revisit Attention Mechanism in Arbitrary Neural Style Transfer

- ICCV 2021
- 百度CV组，南京大学，国防科技大学
- [paper](https://openaccess.thecvf.com/content/ICCV2021/html/Liu_AdaAttN_Revisit_Attention_Mechanism_in_Arbitrary_Neural_Style_Transfer_ICCV_2021_paper.html) | [code](https://github.com/Huage001/AdaAttN)

### 摘要

​	由于快速任意神经网络风格迁移在各类应用中的灵活性，被学术界、工业界和艺术团体广泛关注。现有的方法要么直接将深度风格特征融合到深度内容特征中而不考虑特征分布，要么根据风格自适应的对深度内容特征进行归一化，以让全据统计信息匹配。虽然有效，但浅层信息和局部特征统计没被考虑，它们容易产生不自然的局部分布输出。为了克服这个问题，我们在这篇文章中提出了全新的注意力和归一化模块，称作自适应注意力归一化(**Ada**ptive **Att**ention **N**ormalization, AdaAttN)，逐点的基础上自适应地进行注意力归一化。具体来说，空间注意力评分通过内容和风格图像的浅层和深层特征学习到。然后，将一个风格特征点视为所有风格特征点的注意力加权输出的分布，计算每点的甲醛统计量。最后，进行内容特征的归一化使得它们表现出与驻点加权风格特征同意相同的局部特征统计。此外，在AdaAttN的基础上，我们还提出了一种新的局部特征损失方法用以提高局部视觉质量。我们还对AdaAttN进行扩展，使得它可以稍作修改就能进行视频风格迁移。实验展示出了我们的方法对人意的图像和视频风格迁移任务做到了最先进的结果。

### 贡献

​	在这篇文章里，我们提出了新颖的AdaAttN模块用于任意风格的迁移任务。AdaAttN通过对风格特征的每点进行注意力加权的均值和方差处理，达到特征统计的传递。注意力权重通过特征和内容从低层到高层的全部信息构建。只需通过很小的修改，我们的方法就可以对视频进行风格迁移。实验结果表示我们的方法可以对图像和视频生成高质量的风格迁移结果。AdaAttN有潜力改善其他图像处理或翻译任务，我们将在未来的工作中探索这一点。

### 网络架构

<img src="https://upload-images.jianshu.io/upload_images/12014150-b8757c81bbc85961.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" />

## 代码阅读



## 实验结果

​	在Linux环境中配置该项目，按照官方README中的inference说明进行配置，过程中没有遇到特殊的问题。

​	在进行测试时由于内存限制，需要对图像尺寸进行一定程度的缩小，同时默认情况下图像要求为正方形（如果调整为ratio为小数，有可能在tensor维度中对不齐），因此首先先对图像进行了中心区域的提取和维度的同意，代码如下：

```python
```

​	将会生成``index.html`文件，汇总所有的生成图片。最终的结果可以在[Style Transfer Demo网站](https://doublez0108.github.io/CV/Style-Transfer/style-transfer.html)上查看。

<img src="https://upload-images.jianshu.io/upload_images/12014150-b8f664a505e81525.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" />