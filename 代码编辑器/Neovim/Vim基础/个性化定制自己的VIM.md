# 我的VIM我做主，个性化配置属于自己的VIM
<style> table {margin: auto;} </style>
## 为什么要配置VIM
- （1）Vim中有非常多的配置项，最基本的就是设置显示行号的命令`set number`。
- （2）经过Vim配置后，以后就不需要重新配置需要的功能了。
- （3）Vim提供了`.vimrc`文件用于实现持久化自定义的Vim配置的方式。

## 如何编写Vim配置文件

在Linux系统中，Vim的配置文件在根目录下的一个隐藏文件`.vimrc`，如果没有新建一个，然后我们就可以在其中编辑自己的Vim自定义配置。

Vim配置文件通常包含的内容：
- （1）常用配置，比如`set number`设置显示行号、`colorsheme hybrid`设置主题等；
- （2）常用的映射，比如`noremap <leader>w:w<cr>`设置保存文件的映射；
- （3）自定义的vimscript函数和插件的配置（这个属于Vim的进阶应用）。

## VIM中的映射

Vim映射的概念可以理解为：**把一个操作映射到另一个操作**。比如我们可以使用更方便的快捷键映射原生的Vim快捷键，我们可以按自己的意愿去定制称手的Vim。由于Vim中有很多模式，因此Vim中的映射比较复杂。


**基本映射**
基本映射指在`normal`模式下的映射，比如下面的指令，在正常模式下将`<space>`映射为`viw`（选中单词）：

```
nnoremap <space> viw
```

对于Vim的normal/visual/insert三种模式，我们都可以自定义映射。使用`nmap/vmap/imap`可以实现分别对应于normal/visual/insert三种模式的映射。

| 命令 | 描述 |
|:--|:--|
| `nmap` | normal模式下的映射 |
| `vmap` | visual模式下的映射 |
| `imap` | insert模式下的映射 |


- 设置leader键为`,`的命令为：`let mapleader=','`；
- 在插入模式保存快捷键设置为`,+w`的命令为：`inoremap <leader>w <Esc>:w<cr>`；





**注意：** Vim中的映射概念挺复杂，但是功能非常强大，需要平时的积累。

## VIM插件
现代化的Vim可以通过插件管理安装插件。

- 通过插件我们就可以极大的扩充Vim的功能；
- 想要使用Vim插件，首先需要具备一定的Vim配置知识。

## VIM脚本

Vim具有自己的脚本语言`Vimscript`，对于高级用户可以实现清大的vim插件。