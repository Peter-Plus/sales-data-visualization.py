import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
销售数据 = pd.read_csv("销售记录.csv")

# 提取月份和销售额
月份 = 销售数据["月份"]
销售额 = 销售数据["销售额"]

# 绘制折线图
plt.plot(月份, 销售额)
plt.xlabel("月份")
plt.ylabel("销售额")
plt.title("每月销售额变化趋势")
plt.show()
