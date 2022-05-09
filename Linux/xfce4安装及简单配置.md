
# 利用xfce4给ubuntu终端添加背景图片

## 动机
我使用xfce4的动机：天天看着单调的终端有点枯燥，就想加上一个漂亮的背景图片，当然xfce4的美化功能不仅如此。

## 一、xfce4的安装
```
sudo apt-get install xfce4v
```

## 二、设置xfce4为默认终端

ubuntu提供了一个`update-alternatives`方法修改系统的默认终端，使用法法如下所示：

```
sudo update-alternatives --config x-terminal-emulator
```

在终端输入上述命令，则罗列出系统中可用的终端，每个终端前面都有一个编号，想让谁成为默认终端，可以输入对应终端前面的编号即可，我这里输入5，就把xfce4设置为默认终端了。

<div align=center><img src="../../FullStack/assets/Linux/设置xfce4为默认终端.png"></div>


## 设置xfce4终端字体及添加背景图片

**1、字体设置**

由于使用了`zsh`，所以打开的xfce4的第一步需要重新设置终端字体，不然会出现如下的icon乱码：

<div align=center><img src="../../FullStack/assets/Linux/终端icon乱码.png"></div>

如下图所示，点击终端上面的`编辑`$\to$`首选项`，在弹出选项卡上点击`外观`，然后点击如下图红框，在弹出的对话框汇总选择字体，我这里使用的是`DejaVuSansMono Nerd Font Book`字体，设置完成后，icon乱码的bug修复完成：

<div align=center><img src="../../FullStack/assets/Linux/xfce4终端字体设置.png"></div>

**2、设置背景图片**

如下图所示，在`终端首选项`的`外观`对话框中，点击`背景`的下拉菜单，选择`背景图片`；然后在文件中添加系统中的图片，底纹可以设置背景的透明度：


<div align=center><img src="../../FullStack/assets/Linux/设置背景图片.png"></div>


设置完的最终效果如下图所示：

<div align=center><img src="../../FullStack/assets/Linux/我设置的终端.png"></div>

## 三、彻底卸载xfce4的方法
在安装xfce4的时候会默认安装很多相关软件，如果我们仅仅使用`sudo apt-get remove xfce4`命令，并不能彻底删除xfce4。如果想彻底删除，需要在终端输入如下命令：

```
sudo apt-get purge xfconf xfce4-utils xfwm4 xfce4-session thunar xfdesktop4 \
exo-utils xfce4-panel xfce4-terminal libxfce4util-common scim xscreensaver
```

最后使用如下命令删除残留文件：

```
sudo apt-get autoremove
```