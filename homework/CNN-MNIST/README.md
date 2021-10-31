# 第六次作业 - CNN处理MNIST手写数字识别问题

<center>姓名：张喆	&emsp;&emsp;&emsp;&emsp;	学号：2101212846	&emsp;&emsp;&emsp;&emsp;	指导老师：张健老师</center>

[toc]

-----

## 问题描述

在W6_MNIST_FC.ipynb基础上，增加卷积层结构/增加 dropout或者BN技术等，训练出尽可能高的MNIST分类效果。

## 框架搭建

老师提供的代码已经可以直接运行训练并进行测试，因此大体框架已经比较完善，以下仅做扩展：

- **增加loss和acc绘图模块**

  <img src="https://upload-images.jianshu.io/upload_images/12014150-444ceb15c9a49d4e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" />

- **使用GPU加速**：在model和数据定义与传输部分加入`tocuda()`以使用GPU加速训练过程

- **将全连接网络替换为CNN网络**：将在第三部分详细描述

## CNN网络搭建及实验

首先先搭建基础的CNN网络结构：

- 采用两个卷积层，每个卷积层的`kernel=5` `stride=1` `padding=2`，因此卷积层不改变数据维度
- 每个卷积层之后采用最大池化层进行数据抽象和降维
- 最后通过一层全连接层输出10类分类结果

```python
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.cnn = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2),
            torch.nn.MaxPool2d(kernel_size=2),
            torch.nn.ReLU(),
            torch.nn.Conv2d(16, 32, 5, 1, 2), 
            torch.nn.MaxPool2d(2)
        )
        self.linear = torch.nn.Linear(32*7*7, 10)

    def forward(self, x):
        x = self.cnn(x)
        x = x.view(x.size(0), -1)
        x = self.linear(x)
        output = x
        return output
```

接下来将在基础CNN网络架构上进行一些技术扩建以寻求较优配置，每次运行完记录训练的`loss`和测试的准确性`accuracy`

实验的参数如下：

- `epoch = 2`
- `learning_rate = 0.001`
- `batch_size = 100`
- `Adam`优化器
- `CrossEntropy`损失函数
- 用前2000个测试数据进行测试

| 网络架构            | 训练损失(*loss*) | 测试准确性(*accuracy*) |
| ------------------- | ---------------- | ---------------------- |
| base                | 0.1230           | 0.959                  |
| stride=2代替MaxPool | 0.3318           | 0.914                  |
| 增加BatchNorm       | 0.0647           | 0.970                  |
| 增加Dropout         | 0.2234           | 0.945                  |
| 改用Sigmoid激活函数 | 0.3467           | 0.896                  |
| 增加网络中节点数量  | 0.1190           | 0.971                  |
| 增加网络深度        | 0.0775           | 0.960                  |
| 改进最后全连接网络  | 0.0672           | 0.968                  |

从以上不甚完全的实验中可以看到MaxPool、BatchNorm、增加节点数、增加网络深度、改进全连接等都对训练结果起到比较正向的影响，且部分技术让结果提升比较显著。但该实验由于缺少组合验证以及多次大规模的重复实验，因此不能确定其他技术例如Dropout是否对结果提升有帮助。

## 最终实验结果

最终设置参数如下：

- `epoch = 20`
- `learning_rate = 0.0005`
- `batch_size = 100`

同时增加了数据集扩充方法，并使用全部测试数据进行测试

```python
train_tfm = transforms.Compose([
    transforms.AutoAugment(),
    transforms.RandomAffine(20),
    transforms.RandomRotation(20),
    transforms.ToTensor()
])
```

网络结构定义如下：

```python
self.cnn = torch.nn.Sequential(
  torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2),
  torch.nn.BatchNorm2d(16),
  torch.nn.ReLU(),
  torch.nn.Dropout2d(p=0.1),
  torch.nn.MaxPool2d(kernel_size=2),

  torch.nn.Conv2d(16, 32, 5, 1, 2), 
  torch.nn.BatchNorm2d(32),
  torch.nn.ReLU(),
  torch.nn.Dropout2d(p=0.2),
  torch.nn.MaxPool2d(2),

  torch.nn.Conv2d(32, 64, 5, 1, 2), 
  torch.nn.ReLU(),
  torch.nn.BatchNorm2d(64),
  torch.nn.Dropout2d(p=0.2)
)

self.linear = torch.nn.Sequential(
  torch.nn.Linear(64*7*7, 100), 
  torch.nn.BatchNorm1d(100),
  torch.nn.Dropout(0.2),
  torch.nn.Linear(100, 10),
  torch.nn.ReLU()
)
```

>  最终的准确率`acc=0.992`

![output.png](https://upload-images.jianshu.io/upload_images/12014150-364ba9266ccde2ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 实验中的问题

1. **显存爆炸**：在实验中当网络层过深时由于GPU资源有限会出现out of memory问题，即使在开头指定最多使用80%的资源仍然会有问题

   > 最终找到问题在test的时候依然保留梯度计算导致占用过大，在test部分增加如下代码即可消除内存爆炸问题
   >
   > ```python
   > with torch.no_grad():
   >                 test_output = model(test_x.cuda())
   > ```

2. **激活函数对结果精度和内存消耗的影响**：实验中发现如果先通过激活函数，再进行Dropout、池化等操作当层数加深之后会占用大量内存导致显存爆炸，但在增加的层中不增加激活函数处理则不会有问题；同时增加激活函数可以一定程度上的提升精度

## 附录：实验中网络的实际代码

1. base

   ```python
   self.cnn = torch.nn.Sequential(
   	torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2),
   	torch.nn.MaxPool2d(kernel_size=2),
       torch.nn.ReLU(),
       torch.nn.Conv2d(16, 32, 5, 1, 2), 
       torch.nn.MaxPool2d(2)
   )
   ```

2. stride=2代替MaxPool

   ```python
   self.cnn = torch.nn.Sequential(
   	torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=2, padding=2),
       torch.nn.ReLU(),
       torch.nn.Conv2d(16, 32, 5, 2, 2), 
   )

3. 增加BatchNorm

   ```python
   self.cnn = torch.nn.Sequential(
   	torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2),
   	torch.nn.BatchNorm2d(16),
   	torch.nn.MaxPool2d(kernel_size=2),
       torch.nn.ReLU(),
       torch.nn.Conv2d(16, 32, 5, 1, 2), 
       torch.nn.BatchNorm2d(32),
       torch.nn.MaxPool2d(2)
   )

4. 增加Dropout

   ```python
   self.cnn = torch.nn.Sequential(
   	torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2),
   	torch.nn.Dropout(p=0.2),
   	torch.nn.MaxPool2d(kernel_size=2),
       torch.nn.ReLU(),
       torch.nn.Conv2d(16, 32, 5, 1, 2), 
       torch.nn.Dropout(0.2),
       torch.nn.MaxPool2d(2)
   )

5. 改用Sigmoid激活函数

   ```python
   self.cnn = torch.nn.Sequential(
   	torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2),
   	torch.nn.MaxPool2d(kernel_size=2),
       torch.nn.Sigmoid(),
       torch.nn.Conv2d(16, 32, 5, 1, 2), 
       torch.nn.MaxPool2d(2)
   )

6. 增加网络中节点数量

   ```python
   self.cnn = torch.nn.Sequential(
   	torch.nn.Conv2d(in_channels=1, out_channels=32, kernel_size=5, stride=1, padding=2),
   	torch.nn.MaxPool2d(kernel_size=2),
       torch.nn.ReLU(),
       torch.nn.Conv2d(32, 64, 5, 1, 2), 
       torch.nn.MaxPool2d(2)
   )
   self.linear = torch.nn.Linear(64*7*7, 10)

7. 增加网络深度

   ```python
   self.cnn = torch.nn.Sequential(
   	torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2),
   	torch.nn.MaxPool2d(kernel_size=2),
       torch.nn.ReLU(),
       torch.nn.Conv2d(16, 32, 5, 1, 2), 
       torch.nn.MaxPool2d(2),
       torch.nn.Conv2d(32, 32, 5, 1, 2)
   )

8. 改进最后全连接网络

   ```python
   self.linear = torch.nn.Sequential(
       torch.nn.Linear(32*7*7, 500),
       torch.nn.BatchNorm1d(500),
       torch.nn.Dropout(0.2),
       torch.nn.Linear(500, 10)
   )