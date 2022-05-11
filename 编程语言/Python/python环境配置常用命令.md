

## torch版本号及相关基本信息查询

```python
import torch
# 查询torch版本号
print(torch.__version__)
# 查询torch是否可以使用GPU
print(torch.cuda.is_available())
```

## python版本查询
查询的方法很多，这里罗列两种最常用的：

```python
python -V
```

在有的python环境中上面的命令不好使的时候，可以使用下面的方法：

```python
import sys
# sys模块提供了一系列有关python运行环境的变量与函数

# 查询python版本的变量
print(sys.version)
```
