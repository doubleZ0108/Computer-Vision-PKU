# 第四周作业 - 矩阵导数问题

<center>姓名：张喆	&emsp;&emsp;&emsp;&emsp;	学号：2101212846	&emsp;&emsp;&emsp;&emsp;	指导老师：张健老师</center>

[toc]

## 问题描述

目标函数：$f = ||max(XW, 0)-Y||^2_F$

手动写出以下表达式，并用PyTorch进行验证



## 问题求解

对于本问题，首先不考虑`max()`函数，将原始目标函数进行简化，并令$Z = XW - Y$

则原式F范数的平方问题化简为$f = tr(Z^TZ)$



### $\frac{\partial f}{\partial Y}$

由导数的链式法则，$\frac{\partial f}{\partial Y} = \frac{\partial f}{\partial Z}\frac{\partial Z}{\partial Y}$

- $\frac{\partial f}{\partial Z}$根据公式$\frac{\partial tr(AXBX^T)}{\partial X} = AXB+A^TXB^T$，可化简为$\frac{\partial Z^T Z}{\partial Z} = \frac{\partial Z Z^T}{\partial Z} = EZE+E^TZE^T = 2Z$
- $\frac{\partial Z}{\partial Y} = -1$

综上$\frac{\partial f}{\partial Y} = \frac{\partial f}{\partial Z}\frac{\partial Z}{\partial Y} = -2Z = 2(Y-XW)$



### $\frac{\partial f}{\partial X}$

由导数的链式法则，$\frac{\partial f}{\partial X} = \frac{\partial f}{\partial Z}\frac{\partial Z}{\partial X}$

- $\frac{\partial f}{\partial Z}$在上已经计算
- $\frac{\partial Z}{\partial X}$根据公式$\frac{\partial tr(AB)}{\partial A} = B^T$，可化简为$\frac{\partial (XW-Y)}{\partial X} = \frac{\partial XW}{\partial X} - \frac{\partial Y}{\partial X} = W^T$

综上，$\frac{\partial f}{\partial X} = \frac{\partial f}{\partial Z}\frac{\partial Z}{\partial X} = 2ZW^T$



### $\frac{\partial f}{\partial W}$

同理，$\frac{\partial f}{\partial W} = 2X^TZ$



### 考虑max函数

由于max函数的存在，还需要计算其对各元素的偏导

记函数$\sigma$表达式如下
$$
\sigma_{i j} = \begin{cases}1, & (X W)_{i j}>0 \\ 0, & \text { otherwise }\end{cases}
$$
还需要将之前的计算公式进行修正, $\frac{\partial f}{\partial X} = 2(Z \odot \sigma)W^T$, $\frac{\partial f}{\partial W} = 2X^T(Z \odot \sigma)$，其中$\odot$代表对位相乘

综上

- $\frac{\partial f}{\partial Y} = -2Z = 2(Y-XW)$
- $\frac{\partial f}{\partial X} = 2(Z \odot \sigma)W^T$
- $\frac{\partial f}{\partial W} = 2X^T(Z \odot \sigma)$



## PyTorch验证

```python
import torch
torch.manual_seed(0)
```

```python
x = torch.randn(10, 4, requires_grad=True)
W = torch.randn(4, 4, requires_grad=True)
y = torch.randn(10, 4, requires_grad=True)

print("x: ", x)
print("W: ", W)
print("y: ", y)
```

```
x:  tensor([[-1.1258, -1.1524, -0.2506, -0.4339],
        [ 0.8487,  0.6920, -0.3160, -2.1152],
        [ 0.3223, -1.2633,  0.3500,  0.3081],
        [ 0.1198,  1.2377,  1.1168, -0.2473],
        [-1.3527, -1.6959,  0.5667,  0.7935],
        [ 0.5988, -1.5551, -0.3414,  1.8530],
        [-0.2159, -0.7425,  0.5627,  0.2596],
        [-0.1740, -0.6787,  0.9383,  0.4889],
        [ 1.2032,  0.0845, -1.2001, -0.0048],
        [-0.5181, -0.3067, -1.5810,  1.7066]], requires_grad=True)
W:  tensor([[ 0.2055, -0.4503, -0.5731, -0.5554],
        [ 0.5943,  1.5419,  0.5073, -0.5910],
        [-1.3253,  0.1886, -0.0691, -0.4949],
        [-1.4959, -0.1938,  0.4455,  1.3253]], requires_grad=True)
y:  tensor([[ 1.5091,  2.0820,  1.7067,  2.3804],
        [-1.1256, -0.3170, -1.0925, -0.0852],
        [ 0.3276, -0.7607, -1.5991,  0.0185],
        [-0.7504,  0.1854,  0.6211,  0.6382],
        [-0.0033, -0.5344,  1.1687,  0.3945],
        [ 1.9415,  0.7915, -0.0203, -0.4372],
        [-0.2188, -2.4351, -0.0729, -0.0340],
        [ 0.9625,  0.3492, -0.9215, -0.0562],
        [-0.6227, -0.4637,  1.9218, -0.4025],
        [ 0.1239,  1.1648,  0.9234,  1.3873]], requires_grad=True)
```

```python
q = x.mm(W)
p = torch.max(q, torch.zeros_like(q)) - y
f = torch.trace(p.t().mm(p))
print(f)
```

```
tensor(99.9048, grad_fn=<TraceBackward>)
```

```python
f.backward()

print("W grad: ", W.grad)
print("x grad: ", x.grad)
print("y grad: ", y.grad)
```

```
W grad:  tensor([[ 18.2980,   2.7573,   2.3914,  -0.1974],
        [ 11.0817,   6.6428,   2.5163, -20.3225],
        [ -8.6662,   3.4506,  -1.8979,  -3.3608],
        [-21.1681,  -6.6739,  -1.0693,  27.0278]])
x grad:  tensor([[  1.1002,   0.0860,   5.3377,   0.2788],
        [  0.9583,  10.4633, -13.5234, -16.3639],
        [ -0.8712,  -0.9272,  -0.7764,   2.0790],
        [ -1.4504,   5.6914,   0.7613,  -0.9693],
        [ -1.2892,  -3.4714,  -1.9788,   4.8091],
        [ -4.0523,  -4.3127,  -3.6114,   9.6703],
        [ -0.7312,  -0.7782,  -0.6516,   1.7449],
        [ -0.8191,  -0.8718,  -0.7300,   1.9547],
        [  1.0350,   2.9930,  -6.6743,  -7.5333],
        [ -2.4616,  -2.4243,  -2.1164,   5.7128]])
y grad:  tensor([[ 2.8885e+00,  4.1639e+00,  3.4134e+00,  3.0501e+00],
        [-1.0589e+01, -2.7045e+00, -2.1849e+00, -1.7039e-01],
        [ 6.5523e-01, -1.5214e+00, -3.1982e+00, -1.5687e+00],
        [-1.5009e+00, -3.8551e+00,  4.9843e-01,  1.2764e+00],
        [-6.6077e-03, -1.0689e+00,  1.8791e+00, -4.2604e+00],
        [ 3.8829e+00,  1.5830e+00, -4.0504e-02, -7.2968e+00],
        [-4.3767e-01, -4.8701e+00, -1.4583e-01, -1.3166e+00],
        [ 1.9250e+00,  6.9834e-01, -1.8429e+00, -1.4750e+00],
        [-5.0359e+00, -9.2744e-01,  3.8436e+00, -8.0509e-01],
        [ 2.4780e-01,  2.3296e+00, -1.7491e-01, -4.2519e+00]])
```

```python
q = x.mm(W)
p = torch.max(q, torch.zeros_like(q))
af_ay = 2 * (y - p)
print("af_ay: ", af_ay)

sigma = torch.mm(x, W).detach().numpy()
# print(sigma)
sigma[sigma > 0] = 1
sigma[sigma < 0] = 0
sigma = torch.from_numpy(sigma)
# print(sigma)

z = torch.mm(x, W) - y
af_ax = 2 * torch.mm(z * sigma, W.t())
print("af_ax: ", af_ax)

af_aW = 2 * torch.mm(x.t(), z * sigma)
print("af_aW: ", af_aW)
```

```
af_ay:  tensor([[ 2.8885e+00,  4.1639e+00,  3.4134e+00,  3.0501e+00],
        [-1.0589e+01, -2.7045e+00, -2.1849e+00, -1.7039e-01],
        [ 6.5523e-01, -1.5214e+00, -3.1982e+00, -1.5687e+00],
        [-1.5009e+00, -3.8551e+00,  4.9843e-01,  1.2764e+00],
        [-6.6077e-03, -1.0689e+00,  1.8791e+00, -4.2604e+00],
        [ 3.8829e+00,  1.5830e+00, -4.0504e-02, -7.2968e+00],
        [-4.3767e-01, -4.8701e+00, -1.4583e-01, -1.3166e+00],
        [ 1.9250e+00,  6.9834e-01, -1.8429e+00, -1.4750e+00],
        [-5.0359e+00, -9.2744e-01,  3.8436e+00, -8.0509e-01],
        [ 2.4780e-01,  2.3296e+00, -1.7491e-01, -4.2519e+00]],
       grad_fn=<MulBackward0>)
af_ax:  tensor([[  1.1002,   0.0860,   5.3377,   0.2788],
        [  0.9583,  10.4633, -13.5234, -16.3639],
        [ -0.8712,  -0.9272,  -0.7764,   2.0790],
        [ -1.4504,   5.6914,   0.7613,  -0.9693],
        [ -1.2892,  -3.4714,  -1.9788,   4.8091],
        [ -4.0523,  -4.3127,  -3.6114,   9.6703],
        [ -0.7312,  -0.7782,  -0.6516,   1.7449],
        [ -0.8191,  -0.8718,  -0.7300,   1.9547],
        [  1.0350,   2.9930,  -6.6743,  -7.5333],
        [ -2.4616,  -2.4243,  -2.1164,   5.7128]], grad_fn=<MulBackward0>)
 af_aW:  tensor([[ 18.2980,   2.7573,   2.3914,  -0.1974],
        [ 11.0817,   6.6428,   2.5163, -20.3225],
        [ -8.6662,   3.4506,  -1.8979,  -3.3608],
        [-21.1681,  -6.6739,  -1.0693,  27.0278]], grad_fn=<MulBackward0>)
```

```python
print("x.grad == af_ax ? ", torch.equal(x.grad, af_ax))
print("W.grad == af_aW ? ", torch.equal(W.grad, af_aW))
print("y.grad == af_ay ? ", torch.equal(y.grad, af_ay))
```

```
x.grad == af_ax ?  True
W.grad == af_aW ?  True
y.grad == af_ay ?  True
```

