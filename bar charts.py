import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
销售数据 = pd.read_csv("销售记录.csv")

# 计算每个月商品的平均销售额
每月平均销售额 = 销售数据.groupby("月份")["销售额"].mean()

# 绘制条形图
plt.bar(每月平均销售额.index, 每月平均销售额.values)
plt.xlabel("月份")
plt.ylabel("平均销售额")
plt.title("每月商品平均销售额趋势")
plt.show()
