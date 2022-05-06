
# Pytorch Tensor变换技巧

## 张量的堆叠

结合`torch.unsqueeze()`和`torch.cat()`这两个`torch`的内建函数，我们可以实现两个相同维度的tensor，在新的维度下堆叠。



## 一、torch.unsqueeze()
`torch.unsqueeze()`的作用：在输入张量`input`的`dim`维度上<font color="red">扩展张量维度</font>，并返回一个与输入张量共享内存的新张量，语法格式中的`->`表示共享内存的意思，也就是说改变其中一个张量，另外一个也会改变。

语法格式：
```
torch.unsqueeze(input, dim) -> Tensor
```
参数：
- `input`表示输入张量；
- `dim`表示扩展维度的标号。



下面通过对数学意义上的向量、矩阵、张量进行操作来理解`torch.unsqueeze()`：

1、对向量的操作


## 二、torch.squeeze

`torch.squeeze()`的作用：在输入张量`input`的`dim`维度上扩展张量维度，并返回一个与输入张量共享内存的新张量，语法格式中的`->`表示共享内存的意思，也就是说改变其中一个张量，另外一个也会改变。


语法格式：
```
torch.squeeze(input, dim=None, *, out=None) -> Tensor
```
参数：
- `input`表示输入张量；
- `dim`表示需要压缩的维度，如果不设置，则对所有维度进行压缩操作；如果设置则对指定的维度进行压缩操作；
- `out`表示输出张量。







