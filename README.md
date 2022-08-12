# SquareImageConvert
此程序主要用来将一个非方形的PNG图片，转换成方形的透明背景的PNG图片。

主要应用场景：
- 游戏贴图
- ···

## 前置
- PIL `pip3 install Pillow`进行安装

## 使用方法
在`main.py`同目录创建`origin`文件夹，在文件夹内放置需要转换的png图片。

命令行执行`python3 main.py`，即可在`result`目录下生成转换后的方形图片。