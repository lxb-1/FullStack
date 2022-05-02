

## 下级文件夹与上级文件夹并列的解决

比如我们想在一个文件夹下创建一个子文件夹，但是VScode默认配置下，总会出现如下图所示的下级文件夹总会与上级文件夹并列问题：

<div align=center><img src="../../assets/VScode/上下级文件夹合并.png"></div>

甚至会出现如下图所示的情况：

<div align=center><img src="../../assets/VScode/上下级文件合并1.png"></div>

上面的情况并不是我们想要的结果，解决方法如下所示：

按下打开VScode设置的快捷键`Ctrl+，`，打开设置面板，点击`功能`$\to$`资源管理器`，找到`Compact Folders`，将其前面的$\checkmark$去掉即可。

<div align=center><img src="../../assets/VScode/VScode中设置取消上下级文件合并.png"></div>

这个时候，资源管理器中的文件就恢复上下级别的关系了：

<div align=center><img src="../../assets/VScode/取消上下级文件合并后的效果.png"></div>


## 

​```mermaid
stateDiagram
        [*] --> 激活状态

        state 激活状态 {
            [*] --> NumLock关
            NumLock关 --> NumLock开 : 按下 NumLock 键
            NumLock开 --> NumLock关 : 按下 NumLock 键
            --
            [*] --> CapsLock关
            CapsLock关 --> CapsLock开 : 按下 CapsLock 键
            CapsLock开 --> CapsLock关 : 按下 CapsLock 键
            --
            [*] --> ScrollLock关
            ScrollLock关 --> ScrollLock开 : 按下 ScrollLock 键
            ScrollLock开 --> ScrollLock关 : 按下 ScrollLock 键
        }
​```


​```mermaid
gantt
    title 简单的甘特图
    dateFormat  YYYY-MM-DD
    section 分区1
    任务1-1           :a1, 2014-01-01, 30d
    任务1-2           :after a1  , 20d
    section 分区2
    任务2-1      :2014-01-12  , 12d
    任务2-2      : 24d
​```
 gantt
        苹果 :a, 2017-07-20, 1w
        香蕉 :crit, b, 2017-07-23, 1d
        樱桃 :active, c, after b a, 1d



​```mermaid
stateDiagram
    state "状态描述性文字" as 状态2
​```
