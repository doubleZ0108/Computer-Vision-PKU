# Anaconda安装及使用

* [系统环境](#系统环境)
* [Anaconda GUI](#anaconda-gui)
   * [安装](#安装)
   * [使用](#使用)
* [Anaconda 命令行](#anaconda-命令行)
   * [安装](#安装-1)
   * [使用](#使用-1)
* [Anaconda配置CV所需环境](#anaconda配置cv所需环境)

------

【Anaconda官网】[Anaconda | Individual Edition](https://www.anaconda.com/products/individual#Downloads)



## 系统环境

- 本地**操作系统**：macOS Big Sur 11.6
- 服务器操作系统：Ubuntu 18.04

---

## Anaconda GUI

### 安装

在官网下载安装包，根据提示一步步进行安装即可

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13fa07a0396d49aa870f7f51e78170e6~tplv-k3u1fbpfcp-zoom-1.image" alt="Untitled" width="33%;" />

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53e59177c82e4728a9c77e1532047b26~tplv-k3u1fbpfcp-zoom-1.image" alt="Untitled" width="33%;" />

### 使用

1. 创建虚拟环境

<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47ef0b3e9dec41e79d13d67209f207f7~tplv-k3u1fbpfcp-watermark.image?" alt="Untitled" width="33%;" />

2. 选择所需包进行安装

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47cc2df23b034b518ba028de230c2d93~tplv-k3u1fbpfcp-zoom-1.image" alt="Untitled" width="33%;" />

3. 在IDE中使用虚拟环境进行测试

> 需要安装`ipykernel`

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/034130a688304017844f8b95b410a599~tplv-k3u1fbpfcp-zoom-1.image" alt="Untitled" width="33%;" />

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8663ddc7d78a4851915022e8fe188aba~tplv-k3u1fbpfcp-zoom-1.image" alt="Untitled" width="33%;" />

4. 删除虚拟环境

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f4963d810f04b348fe0c3439de6d4cb~tplv-k3u1fbpfcp-zoom-1.image" alt="Untitled" width="33%;" />

---

## Anaconda 命令行

### 安装

1. 在官网下载Anaconda安装包
2. 按照官网建议通过SHA-256验证数据的正确性

    ```bash
    sha256sum /path/filename
    ```

3. 运行shell脚本
4. 根据提示进行安装
5. 写入环境变量
6. 最后通过`conda —version`验证是否安装成功

> 由于服务器上之前已经安装好Anaconda，这里不再展示安装步骤截图

### 使用

```bash
# 创建虚拟环境
conda create -n [env_name]

# 查看所有环境信息
conda info --envs

# 激活某个环境
conda activate [env_name]

# 退出激活的环境
conda deactivate

# 删除某个环境
conda remove -n [env_name] --all
```

下图为在Ubuntu下的实际操作：

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1060ba6547144eb483c6ee05e65c479f~tplv-k3u1fbpfcp-zoom-1.image" alt="2d139ec1110010c1ce68b1dc3f6a9b65.png" width=" 50%;" />

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3238b4b5bfdb43bd9a6dcc62eec0647d~tplv-k3u1fbpfcp-zoom-1.image" alt="273008e3d2bccaa9002b389578fd9661.png" width="50%;" />

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e25d3e10aaf842cdb881050b2c7476f1~tplv-k3u1fbpfcp-zoom-1.image" alt="9666e3ea2098f32288bbfdfd2c3b8836.png" width="50%;" />

---

## Anaconda配置CV所需环境

由于最新版的anaconda默认python版本是3.8导致opencv不支持，因此首先把conda的python版本降为3.7

```bash
conda install python=3.7 anaconda=custom
```

之后创建虚拟环境并安装所需python包

```bash
conda create -n cv
conda activate cv
conda install opencv, numpy, matplotlib
```

<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bbc4f09b3424a6daae657034e266906~tplv-k3u1fbpfcp-zoom-1.image" alt="Untitled" width="50%;" />



