# wCloud-WebApp
一个基于flask和[wCloud](https://github.com/sepinetam/wcloud)的Web App

# 多语言导航
- [ENGLISH](README.md)
- [中文](README.CN.md)

# 版本
@Version0.0.1

# 如何使用
你可以通过进入项目[官方网站](https://wcloud.tools.sepinetam.com)或者克隆该项目到本地使用。

## 官网使用
进入项目[官方网站](https://wcloud.tools.sepinetam.com)，然后按照下面的说法做：
- 上传你的文本文件，受支持的扩展有 ```['txt', 'md']```
- 选择停词文件或者上传你自己的 ```'txt'``` 格式的停词文件.
- 按照你的需求选择其余选项
- 点击 ```生成词云✅``` 按钮

## 本地使用
克隆项目到本地并且运行 ```app.py```
```bash
git clone https://github.com/sepinetam/wcloud-webapp.git
cd wcloud-webapp

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python app.py
```
然后打开你的浏览器(个人更喜欢Google Chrome)并导航到 ```127.0.0.1:5000``` </br>
你将会看到与[官网](https://wcloud.tools.sepinetam.com)一样的页面。

# 致谢
## 字体来源
感谢[恒星中国@StellarCN](https://github.com/StellarCN)在[repo](https://github.com/StellarCN/scp_zh)中提供的中文字体，期待恒星中国发展越来越好。

## 项目需求
感谢上海大学社会学院同学[顾萌](mailto:esme2004dash@163.com)提供的需求，让我能想起来写这么个小工具。
