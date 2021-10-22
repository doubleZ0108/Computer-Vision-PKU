# 第五周作业 - 搭建两层全连接网络

<center>姓名：张喆	&emsp;&emsp;&emsp;&emsp;	学号：2101212846	&emsp;&emsp;&emsp;&emsp;	指导老师：张健老师</center>

[toc]

## 问题描述

<img src="https://upload-images.jianshu.io/upload_images/12014150-61678887c8186205.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" />

## PyTorch实践

### 补全全连接网络结构

在网络`Net()`定义中进行完善

```python
def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(n_feature, n_hidden, bias=True),
            torch.nn.Sigmoid(),
            torch.nn.Linear(n_hidden, n_output, bias=True)
        )
def forward(self, x):
        x = self.net(x)
        return x
```

或将隐藏层和输出层单独构建

```python
def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden, bias=True)
        self.predict = torch.nn.Linear(n_hidden, n_output, bias=True)
def forward(self, x):
        x = F.sigmoid(self.hidden(x))
        x = self.predict(x)
        return x
```

其他代码保持不变进行训练，发现经过200次迭代之后仍然无法收敛，结果如下左图所示：

<div align="center"><img src="https://upload-images.jianshu.io/upload_images/12014150-c38896fc4088d09d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" /><img src="https://upload-images.jianshu.io/upload_images/12014150-8d22dd02663ad394.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" /></div>

增加迭代轮次到2000，发现模型在1500轮左右能够比较好的拟合，如上右图所示

但该模型可能过拟合，对最终的模型进行测试(其中rand产生的随机值压缩比例改为0.4)，结果如下，可以看到其对分布略有偏差的数据集拟合效果并不完美

<img src="https://upload-images.jianshu.io/upload_images/12014150-d70115093eb4b976.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" />

### 激活函数改进

在使用规定的sigmoid中发现，模型在前1000次训练时几乎都卡在初始状态，只有当迭代足够多次时才能拟合，猜想是激活函数选取的不是很妥当，改为使用relu函数，并仅训练200次，结果如下左图，可以看到当前模型拟合虽然不完美，但并没有sigmoid激活函数训练200次类似的“水平”问题，继续增加训练次数倒2000轮，效果如右图所示，从结果中来看，并没有sigmoid激活函数训练同样轮次的模型平滑

<div align="center"><img src="https://upload-images.jianshu.io/upload_images/12014150-98b7ce225b023882.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" /><img src="https://upload-images.jianshu.io/upload_images/12014150-8f9eeb2c89e12a47.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" /></div>

## 推导变量导数表达式

由原始定义
$$
\begin{aligned}
&h=X W_{1}+b_{1} \\
&h_{\text {sigmoid }}=\operatorname{sigmoid}(h) \\
&Y_{\text {pred }}=h_{\text {sigmoid }} W_{2}+b_{2} \\
&f=\left\|Y-Y_{\text {pred }}\right\|_{F}^{2}
\end{aligned}
$$

得

$$
\frac{\partial f}{\partial Y_{pred}} = 2(Y_{pred} - Y)
$$

$$
\frac{\partial f}{\partial h_{sigmoid}} = \frac{\partial f}{\partial Y_{pred}}W_2^T
$$

$$
\frac{\partial f}{\partial W_2} = h_{sigmoid}^T \frac{\partial f}{\partial Y_{pred}}, \ \frac{\partial f}{\partial b_2} = \frac{\partial f}{\partial Y_{pred}}
$$

$$
\frac{\partial f}{\partial h} = \frac{\partial f}{\partial h_{sigmoid}} \odot sigmoid'(h), \ sigmoid'(x) = sigmoid(x)(1-sigmoid(x))
$$

$$
\frac{\partial f}{\partial W_1} = X^T \frac{\partial f}{\partial h}, \ \frac{\partial f}{\partial b_1} = \frac{\partial f}{\partial h}
$$

综上

- $\frac{\partial f}{\partial W_1} = (2X^T(Y_{pred}-Y)W_2^T) \odot (sigmoid(h)(1-sigmoid(h)))$
- $\frac{\partial f}{\partial b_1} = (2(Y_{pred}-Y)W_2^T) \odot (sigmoid(h)(1-sigmoid(h)))$
- $\frac{\partial f}{\partial W_2} = 2h_{sigmoid}^T(Y_{pred}-Y)$
- $\frac{\partial f}{\partial b_2} = 2(Y_{pred} - Y)$

