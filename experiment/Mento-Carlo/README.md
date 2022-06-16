# 算法第十四次作业

<center>姓名：张喆	&emsp;&emsp;&emsp;&emsp;	学号：2101212846	&emsp;&emsp;&emsp;&emsp;	指导老师：张健老师</center>

## 实验要求

写一个程序，用蒙特卡洛法求圆周率pi

## 实验思路

蒙特卡洛算法的核心思想是“repeated random sampling to obtain numerical results”

因此实验首先划定$[0,1]\times[1,0]$的单位空间，随机生成$N$个点，计算点落入$x^2+y^2<=1, (0 \leq x \leq 1,0\leq y \le1)$中的个数占总体的比例，以此逼近$\pi$

## 实验结果

随机撒落1000个点进行模拟，最终拟合的结果$\hat \pi = 3.156$

![b3b9578a-1085-41e7-8477-94f970db0d7d.png](https://upload-images.jianshu.io/upload_images/12014150-5175a7e1d63c0917.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

又从100～100000进行更多的实验，绘制曲线如下，可以观察到由于蒙特卡洛算法的随机性，即使增大到非常大量的数量级，依然存在着拟合的波动（并不像期待的平滑曲线不断趋近真值），但随着点数的增加拟合效果的偶然性更小，结果理论上更可信

![c62b8f82-0557-45c3-bcd0-dc3332ea1793.png](https://upload-images.jianshu.io/upload_images/12014150-bc01fbdfc17727d9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 代码

```python
import numpy as np
import matplotlib.pyplot as plt

totalNum = 100

x, y = np.random.rand((totalNum)), np.random.rand((totalNum))
my_pi = np.where(np.sqrt(x**2 + y**2) < 1)[0].shape[0] / totalNum * 4
print(my_pi)

plt.figure(figsize=(5,5))
plt.scatter(x, y)
circle = plt.Circle((0,0), 1, color='r', fill=False)
plt.gcf().gca().add_artist(circle)
plt.show()
```

```python
X, Y = [], []
for totalNum in range(100, 100000, 500):
    x, y = np.random.rand((totalNum)), np.random.rand((totalNum))
    X.append(totalNum)
    Y.append(np.where(np.sqrt(x**2 + y**2) < 1)[0].shape[0] / totalNum * 4)

plt.plot(X, Y)

plt.plot([0, X[-1]], [np.pi, np.pi], 'r--')
plt.annotate(np.pi,
                xy=(X[len(X)//2], np.pi), xycoords='data', 
                xytext=(-30, -40), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
```

