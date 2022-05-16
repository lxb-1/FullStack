# tmux常用快捷方式及操作命令
<style> table {margin: auto;} </style>
## 前言



tumx可以实现Linux多会话操作，即在一个**在一个会话中进行多窗口的操作**；另外，在使用xshell等远程服务时，tumx可以实现重新链接时的操作保留功能，从而提高我们的工作效率，tmux的具体特点如下所示：

> **tmux的特点：**
> （1）在单个会话窗口中，分割多个窗口，实现多个会话操作，以实现同时运行多个命令行程序；
> （2）能够实现新建窗口“接入”已经存在的会话；
> （3）能够实现每个会话链接多个窗口，提供多人实时共享会话功能。


## 常用快捷键及操作指令

| 快捷键 | 功能 | tmux指令 |
|:--|:--|:--|
| `Ctrl+b s` | 查看所有tmux会话 | `tmux ls` |
| - | 新建tmux窗口 | `tmux new -s <session_name>` |
| `Ctrl+b $` | 重命名会话 | `tmux rename-session -t`<br>`<old_name> <new_name>` |
| `Ctrl+b d` | 分离会话 | `tmux detach`或`exit` |
| - | 重链会话 | `tmux attach -t <session_name>`或<br>`tmux at -t <session_name>` |
| `Ctrl+b z` | 平铺当前窗格 | - |
| - | 杀死会话 | `tmux kill-session -t <session_name>` |
| - | 切换会话 | `tmux switch -t <session_name>` |
| - | 切换会话 | `tmux switch -t <session_name>` |