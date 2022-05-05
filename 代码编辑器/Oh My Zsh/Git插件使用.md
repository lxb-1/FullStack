
## Oh My zsh中git插件的使用简介

在`~/.zshrc`中添加`git`插件的方法如下图所示，如果配置文件中没有`git`插件，可以将其添加上即可：

<div align=center><img src="../../assets/Oh%20My%20Zsh/zsh安装git插件的方法.png"></div>


安装的插件放在如上图的红框中的目录地址中。如下图所示，安装的git插件文件夹中有两个文件：
- （1） `git.plugin.zsh`：git插件配置文件；
- （2） `README.md`：个it插件使用手册。

<div align=center><img src="../../assets/Oh%20My%20Zsh/zsh中git插件的内容.png"></div>

其实，其他插件也是这种存放格式，通过这种方式我们可快速了解Oh My zsh相关插件的具体内容。

这里罗列几个常用的作为示例展示它们的作用：

| 快捷键 | git命令 | 描述 |
|:--|:--|:--|
| `gaa` | `git add --all` | 添加当前项目所有文件修改、增删的文件到缓存区 |
| `gbD` | `git branch -D` | 删除分支 |
| `gcam` | `git commit -a -m` | 提交项目到本地库，其中`-a`表示不用再次输入`git add`命令 |
| `gcb` | `git checkout -b` | 将特定分支上暂存储区的内容替换当下工作区的内容，<br> 比如，`git checkout -b dev/1.5.4 origin/dev/1.5.4` <br> 表示从远程`dev/1.5.4`分支提取到本地分支的`1.5.4` |
| `gcm` | `git checkout master` | 取出`master`版本的`HEAD` |

其实，如果了解了Oh My Zsh中插件使用的过程，我们会认识到：<font color="red">工具只是工具，我们熟练使用这些工具的基础还是Git的原理。</font>
