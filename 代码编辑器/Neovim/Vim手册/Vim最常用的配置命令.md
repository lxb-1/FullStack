
# VIM最常用的配置命令

## VIM的自动换行及自动折行设置

**自动换行**

这里以`.vimrc`文件中的设置为例：
自动换行是每行超过`n`个字的时候vim自动加上换行符。需要注意的是，如果一个段落的首个单词很长，查处了自动换行设置的字符则不会换行。但是，对于中文文本，由于文字之间没有空格，所以通常不会触发自动换行，只有输入新的文本才会触发。

对于已经存在的文本，我们可以通过选中它们，然后按下`gq`就可以实现自动换行了。

下面的指令可以设置每行文本的长度：

```
set textwidth=78
```

如果想实现对于中文文本的自动换行，可以通过下面的命令实现：
```
set formatoptions+=mM
```
其中，
- （1）`m`：Also break at a multi-byte character above 255. This is useful for Asian text where every character is a word on its own.
- （2）`M`：When joining lines, don't insert a space before or after a multi-byte character. Overrules the 'B' flag.


**自动折行**
自动折行是把长的一行用多行显示，不在文件中加换行符：

```
set wrap    # 设置自动折行
set nowrap  # 设置不自动折行
```
