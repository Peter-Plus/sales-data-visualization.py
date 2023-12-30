import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
销售数据 = pd.read_csv("销售记录.csv")

# 计算每个商品的总销售额
商品销售额 = 销售数据.groupby("商品")["销售额"].sum()

# 绘制饼图
plt.pie(商品销售额.values, labels=商品销售额.index, autopct="%1.1f%%")
plt.title("各商品销售额占比")
plt.show()
