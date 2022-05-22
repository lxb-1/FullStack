# npm、node.js、yarn简介

## npm简介

在介绍npm是什么之前，我们需要首先了解为什么要使用npm。对于程序员通常会遇到这样的问题：

当一个网站所依赖的javascript（js）代码逐渐增加时，我们需要到jQuery官网上下载jQuery、到BootStrap官网上下载BootStrap、到Underscore官网下载Underscore等等，为了解决这个问题，npm就营运而生了。

npm是 **Node package Manager**的缩写，npm是用来管理js的。npm是Node.js默认的包管理工具，也是世界上最大的软件注册表，同时也是世界上最大的软件仓库。

npm的工作原理为：
- 1、通过一个远程代码仓库`register`来管理需要共享的js文件，且每个js文件都具有唯一的标识；
- 2、通过引用远程仓库中js文件的唯一标识，用户就可以自动下载相应的js文件了。

## Node.js简介

Node.js是基于Chrome的跨平台JavaScript运行环境，以便实现在服务器端执行js代码。通过Node.js可以很方便地构建后端应用程序，同时还可以为全栈与前端提供各种解决方案。

Node.js内置了npm，进而在实际开发中，可以很方便的通过npm来共享js代码。我们可以很方便的通过`npm install jquery bootstrap underscore`下载jquery bootstrap underscore代码了，极大的提升了程序员开发效率。



**Ubuntu系统安装node.js与npm**

Node.js与npm的安装有很多方式，这里只给出一种安装方式，在终端输入如下的指令即可安装：

```bash
sudo apt update
sudo apt install nodejs npm
```


## Yarn简介——npm的最大竞争者

Yarn是一款新的JavaScript包管理工具，它的目的是解决在团队项目管理中npm面临的两大问题：

- **一致性问题：** 软件安装时无法保证速度的一致性问题；
- **安全性问题：** 由于npm安装时，允许运行代码，无法保证安全。

但是，Yarn同样是一个从npm注册源获取模板的CLI客户端，其注册方式不会有任何变化，也就是说我们可以以正常的进行包的获取与发布。

Ubuntu系统上最简单的安装方法是使用npm安装：

```
npm install -g yarn
```

## npm与yarn换源——实际应用前首要考虑的第一个问题

npm与yarn的默认镜像在国外，国内访问速度很慢，通常我们会将它们转换为淘宝源：


**npm换源**

```bash
# 查看npm现有源
npm config get register
# 更改npm为淘宝源
npm config set register https://register.npm.taobao.org
```

**yarn换源**

```bash
# 查看yarn现有源
yarn config get register
# 更改yarn为淘宝源
yarn config set register https://register.npm.taobao.org
```
