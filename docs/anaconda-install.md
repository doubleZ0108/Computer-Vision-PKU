# Anaconda安装及使用



【Anaconda官网】

[Anaconda | Individual Edition](https://www.anaconda.com/products/individual#Downloads)



## 系统环境

- 本地**操作系统**：macOS Big Sur 11.6
- 服务器操作系统：Ubuntu 18.04

---

## Anaconda GUI

### 安装

在官网下载安装包，根据提示一步步进行安装即可

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/22f62a76-d2b2-440e-a4d8-2b4b82314cc1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T033750Z&X-Amz-Expires=86400&X-Amz-Signature=20a59ef6b536a5b28def7150915ed5e162bbc396939f5a947f64eabac930420e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" alt="Untitled" width=" 33%;" />

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/04546423-98e1-4f4e-918a-d3951f4e0ba7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T033812Z&X-Amz-Expires=86400&X-Amz-Signature=f36d3c0e22ce5fb2e334658d7c48a82f2a10c49fdef974442f800b217ae6d1d0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" alt="Untitled" width=" 33%;" />

### 使用

1. 创建虚拟环境

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9c9da921-e3fb-4fae-b770-c6b3615e077f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T033837Z&X-Amz-Expires=86400&X-Amz-Signature=6fcbf15259ec39376d5fec1f440f9d1998a158a377c7b38a7d0b0cd5effba348&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" alt="Untitled" width="33%;" />

2. 选择所需包进行安装

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/40d21acf-044f-4a29-a3ce-0d5beddbcbeb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T033847Z&X-Amz-Expires=86400&X-Amz-Signature=daa7e9a1d4f16b4c60c2436f5de77349a7446060c80a2894a76c1dc0b5ffbeb4&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" alt="Untitled" width="33%;" />

3. 在IDE中使用虚拟环境进行测试

> 需要安装`ipykernel`

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3cb8f0ff-5459-4919-9de8-0b7ff93764de/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T033911Z&X-Amz-Expires=86400&X-Amz-Signature=b59a152991ee53030695fd2e13b99a8a85fdc10d0d3c810d901b290676a36f73&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" alt="Untitled" width="33%;" />

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f25dfacf-76d7-4967-9f28-20a1cb8d64da/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T033932Z&X-Amz-Expires=86400&X-Amz-Signature=5c34efee74ce09ca308816e4ecd9077d56a4ed8236731152983520ee7a64d227&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" alt="Untitled" width="33%;" />

4. 删除虚拟环境

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c85e2f91-6054-4001-a229-3cc10f83c99e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T033943Z&X-Amz-Expires=86400&X-Amz-Signature=c076a686bdcaf07237c0e949071a315701113213c7043355a53900c5b274e1fb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" alt="Untitled" width="33%;" />

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

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/177f14e0-54df-4a58-a8e5-03927bb1dd1b/2d139ec1110010c1ce68b1dc3f6a9b65.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T033956Z&X-Amz-Expires=86400&X-Amz-Signature=091d1eb448dbd7649480b2df0523be89c0fbae81d811a654662d5f51bb73a16e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%222d139ec1110010c1ce68b1dc3f6a9b65.png%22" alt="2d139ec1110010c1ce68b1dc3f6a9b65.png" width=" 50%;" />

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8117d330-51ef-4f70-a377-b98e9bcae801/273008e3d2bccaa9002b389578fd9661.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T034006Z&X-Amz-Expires=86400&X-Amz-Signature=2f056de0588c97b466f5de27690800e5932f574480d5eeb171fffb38d2777a38&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22273008e3d2bccaa9002b389578fd9661.png%22" alt="273008e3d2bccaa9002b389578fd9661.png" width="50%;" />

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8e69c9da-3058-4f4d-aefb-57ec38e4e735/9666e3ea2098f32288bbfdfd2c3b8836.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T034015Z&X-Amz-Expires=86400&X-Amz-Signature=8bc144b0c0f55b08433e72a773dbcf5b35aa9e5313aa7fed4ed4f40cf9bcd0eb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%229666e3ea2098f32288bbfdfd2c3b8836.png%22" alt="9666e3ea2098f32288bbfdfd2c3b8836.png" width="50%;" />

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

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ab7fc463-1c78-4b88-b137-a3ad8110354f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210926T034024Z&X-Amz-Expires=86400&X-Amz-Signature=e2dc7a184694e524051112b6c39165e68bf75b2607f56b6ad734280279b93b15&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" alt="Untitled" width="50%;" />