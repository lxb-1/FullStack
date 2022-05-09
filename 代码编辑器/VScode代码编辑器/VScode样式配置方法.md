
VSocde是即与浏览器技术栈，所以可以注入自定义的css，其基本原理是：修改`scode/electron`的主界面文件`workbench.html`，内联了诸如的样式及`js`。

## VScode主题颜色配置关键字

1、基本信息配置关键字
| 关键字 | 描述 |
|:--|:--|
| `contrastActiveBorder` | 当前文件标签外的边框颜色 |
| `contrastBorder` | 在元素周围额外的一层边框(这句话表述的并不是很贴切) |
| `widget.shadow` | 编辑器内小组件的阴影颜色，比如查找/替换等 |
| `progressBar.background` | 进度条的背景颜色 |
| `foreground` | 整体前景色（这句话表述的不准确，我测试的是当前文件路径的字体颜色） |
| `icon.foreground` | 工作台中图标的默认颜色(我测试的是资源管理器文件夹前面图标的颜色) |
| `imagePreview.border` | 图片边框颜色 |
| `errorForeground` | 错误信息的整体前景色，颜色仅在不被组件覆盖时适用e |


2、标题栏配置关键字

| 关键字 | 描述 |
|:--|:--|
| `titleBar.activeBackground` | 活动窗标题栏背景色(我这里怎么设置不了？) |
| `titleBar.activeForeground` | 活动窗标题栏前景色(我这里怎么设置不了？) |
| `activeBorder.activeFocusBorder` | 按下活动栏选中项的边框颜色 |
| `activityBar.background` | 活动栏背景颜色 |
| `activityBar.border` | 活动栏与其他栏的分割线颜色 |
| `activityBar.foreground` | 活动栏中项目图标线条颜色 |
| `activityBar.inactiveForeground` | 活动栏图标颜色 |
| `activityBarBadge.background` | 活动栏徽章（角标）背景色 |
| `activityBarBadge.foreground` | 活动栏徽章（角标）前景色 |
| `badge.background` | 信息标签背景色 |
| `badge.foreground` | 信息标签前景色 |
| `errorForeground` | 错误信息的整体前景色，颜色仅在不被组件覆盖时适用 |


3、活动栏配置关键字

| 关键字 | 描述 |
|:--|:--|
| `activityBar.activeBackground` | 活动栏当前选中项的背景颜色 |
| `activityBar.activeBorder` | 活动栏中当前选中项中靠近窗口边缘处的竖线颜色 |
| `activeBorder.activeFocusBorder` | 按下活动栏选中项的边框颜色 |
| `activityBar.background` | 活动栏背景颜色 |
| `activityBar.border` | 活动栏与其他栏的分割线颜色 |
| `activityBar.foreground` | 活动栏中项目图标线条颜色 |
| `activityBar.inactiveForeground` | 活动栏图标颜色 |
| `activityBarBadge.background` | 活动栏徽章（角标）背景色 |
| `activityBarBadge.foreground` | 活动栏徽章（角标）前景色 |
| `badge.background` | 信息标签背景色 |
| `badge.foreground` | 信息标签前景色 |
| `errorForeground` | 错误信息的整体前景色，颜色仅在不被组件覆盖时适用 |
