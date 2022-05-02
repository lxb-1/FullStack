# 如下的代码是实现Euler-Maruyama方法的python代码，该方法可以解决Ornstein-Uhlenbeck过程。关于理论部分可以参考Euler-Maruyama.md中的内容。
# 代码引用Wiki百科中的示例代码，其网址为：https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method

import numpy as np
import matplotlib.pyplot as plt

num_sims = 5    # 显示五个仿真结果

t_init = 3      # 起始时间
t_end  = 7      # 结束时间
N      = 1000   # 计算1000个样本点
dt     = float(t_end - t_init) / N  # 时间步长
y_init = 0      # 计算基准点

# 表征Ornstein-Uhlenbeck过程偏微分方程的三个参数，
# 本代码中是将这三个参数作为超参数处理的。
c_theta = 0.7
c_mu    = 1.5
c_sigma = 0.06

# 下面三个函数是求解Ornstein-Uhlenbeck过程参数的方法
def mu(y, t):
    # 计算方法为：\theta (\mu - Y_t)
    return c_theta * (c_mu - y)

def sigma(y, t):
    # 计算方法为：直接返回其本身即可
    return c_sigma

def dW(delta_t):
    # 计算方法：对于时间步长的每次调用生成一个服从正态分布
    # 的随机数，其均值为0，标准差为时间步长的开方根。
    return np.random.normal(loc=0, scale=np.sqrt(delta_t))

# np数据格式的时间步长
ts = np.arange(t_init, t_end + dt, dt)
x = print(len(ts))

# 申请一个包含N个采样点的计算结果y的numpy一维矩阵，
# 并设定初始状态ys[0]
ys = np.zeros(N + 1)
ys[0] = y_init

for _ in range(num_sims):
    for i in range(1, ts.size):
        t     = t_init + (i-1) * dt
        y     = ys[i-1]
        ys[i] = y + mu(y, t) * dt + sigma(y,t) * dW(dt)
    plt.plot(ts, ys)

plt.xlabel("time (s)")
h = plt.ylabel("y")
# h.set_rotaion(0)
plt.show()