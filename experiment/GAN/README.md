# 第八次作业 - 生成对抗网络GAN

<center>姓名：张喆	&emsp;&emsp;&emsp;&emsp;	学号：2101212846	&emsp;&emsp;&emsp;&emsp;	指导老师：张健老师</center>

## 论文阅读总结

​	所选论文为经典的GAN开山之作: [Generative Adversarial nets](https://arxiv.org/abs/1406.2661)。

​	GAN的核心思想是构建两个模型：生成器模型G和判别器模型D。G用于捕捉原始数据的分布模式，即尽可能将输入的随机分布数据变为满足期望数据的分布模式；D要求尽可能将G生成的数据和原数据进行区分。整个过程类似于minimax的双人博弈问题，而博弈的最优解是G生成的数据与原始训练数据一模一样，而D判别数据时恒等于$\frac{1}{2}$，即完全无法将G生成的数据和原始数据进行区分。

​	GAN的思想可以用造假币和警察的故事进行比喻：造假币的人试图学习如何骗过警察，而警察需要从很多钱中发现假币的存在，最开始造假币的人可能并不会造假币，很容易就被识破，而最开始警察也难以发现制作精湛的假币，但随着二者的不断迭代成长，造假币人的技术不断精湛，警察甄别假币的能力也不断提升。从某种程度上说，G和D学习到了之前未掌握的方法和模式。如作者在最后部分说到的，生成网络并不是直接通过数据样本进行更新，而是通过判别器判别后的梯度进行更新的。

​	GAN所要优化的函数如下所示。式中第一项代表最大化判别器D正确识别真数据，第二项代表最小化生成器生成的G通过D辨别后被识别的值。
$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\text {data }}(\boldsymbol{x})}[\log D(\boldsymbol{x})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$
​	在论文中，作者还通过详细的推导证明如下两个命题：

1. 对于固定的G，最优的判别器为$D_{G}^{*}(\boldsymbol{x})=\frac{p_{\text {data }}(\boldsymbol{x})}{p_{\text {data }}(\boldsymbol{x})+p_{g}(\boldsymbol{x})}$
2. 如果每一步迭代D都能达到上述(1)中完美分类的话，按照$p_g$更新的标准$\mathbb{E}_{\boldsymbol{x} \sim p_{\text {data }}}\left[\log D_{G}^{*}(\boldsymbol{x})\right]+\mathbb{E}_{\boldsymbol{x} \sim p_{g}}\left[\log \left(1-D_{G}^{*}(\boldsymbol{x})\right)\right]$，$p_g$将最终收敛到$p_{data}$上

​	在真正构建训练时作者也采取了一些其他策略进行简化和优化：1）k次更新D，1次更新G（但在实验中k=1） 2）将G的优化问题从$log(1-D(G(z)))$放缩为$logD(G(z))$，主要用于解决梯度过小不好训练的问题。

​	经过了在MNIST、Toronto人脸数据集、CIFAR-10数据集上的实验，作者指出GAN确实学习到了数据的分布特征而不单纯的是记住了数据集中的数据样本，同时作者也想强调了生成的图片没有经过精心挑选，是很可靠的。

​	最后作者也指出了未来可进行扩展的方向，这些方向也正是后续GAN被广泛应用和优化的大方向，从中足见GAN初创团队理解的深入和远见：

- 对G和D引入条件生成模型$p(x|c)$
- 构建辅助网络首先将$x$变为$z$再进行学习
- 通过引入数据的真值标签进行半自监督的学习
- 通过更好的协调G和D，或采用更好的分布采样z可能加速训练

## 代码分析

​	依照论文中的核心算法部分，代码实现中的相应代码如下：

```python
# ========== Train Generator ========== #
# Sample noise as generator input 输入的随机分布数据
z = Variable(Tensor(np.random.normal(0, 1, (imgs.shape[0], opt.latent_dim))))

# Generate a batch of images 通过生成器处理随机分布数据，希望骗过D
gen_imgs = generator(z)

# Loss measures generator's ability to fool the discriminator
# 生成器loss 论文中公式(1)G的部分，同时进行简化 logD(G(z))
g_loss = adversarial_loss(discriminator(gen_imgs), valid)

#  ========== Train Discriminator ========== #
# Measure discriminator's ability to classify real from generated samples
# 判别器loss
real_loss = adversarial_loss(discriminator(real_imgs), valid)
fake_loss = adversarial_loss(discriminator(gen_imgs.detach()), fake)
d_loss = (real_loss + fake_loss) / 2
```

<center><img src="https://upload-images.jianshu.io/upload_images/12014150-37904458450ee498.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20211116084917478" style="zoom:20%;" /></center>

​	生成器和判别器的网络结构在代码中的定义如下：

<center><img src="https://upload-images.jianshu.io/upload_images/12014150-8f4b51e250c6ba9c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20211116090050475" style="zoom:35%;" /></center>

## 实验结果

​	通过[PyTorch-GAN](https://github.com/eriklindernoren/PyTorch-GAN/blob/master/implementations/gan/gan.py)中的开源代码进行实验，共训练186400 step，记录训练过程中的生成效果，汇总如下：

<center><img src="https://upload-images.jianshu.io/upload_images/12014150-7ef0153d2bdd8613.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20211116091537106" style="zoom:65%;" /></center>

