import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data = {
#     'China': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2500],
#     'America': [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],
#     'Britain': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
#     "Russia": [800, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
# }
# df = pd.DataFrame(data)



df = pd.read_csv("CLDAP_MSSQL_NETBIOS_UDP_Day1.TimeStat_v1_AvgLen.csv", encoding='utf-8')
df.astype(float)


#matplotlib库画箱型图
# df.plot.box(title="Average size of payload")
# plt.grid(linestyle="--", alpha=0.3)
# plt.show()

# # Seaborn库画箱型图
# plt.figure(figsize=(15,5))
# plt.title("Distribution of average payload size")
# plt.xlabel('Average paylaod size (B)')
#
# sns.boxplot(data=df, width=0.8, linewidth=0.5, fliersize=0, orient="h")
# plt.grid(linestyle="--", alpha=0.3)
#
# plt.show()

# 画1*4子图
fig, axes = plt.subplots(1,4)
fig.subplots_adjust(hspace=0.5, wspace=0.5)

sns.boxplot(data=df[["CLDAP"]], ax=axes[0], saturation=1, linewidth=1, fliersize=0.1)
axes[0].set_ylabel("Average packet size (B)")

sns.boxplot(data=df[["MSSQL"]], ax=axes[1], color='orange', saturation=1, linewidth=1, fliersize=0.1)
sns.boxplot(data=df[["NETBIOS"]], ax=axes[2], color='seagreen', saturation=1, linewidth=1, fliersize=0.1)
sns.boxplot(data=df[["UDP-other"]], ax=axes[3], color='firebrick', saturation=1, linewidth=1, fliersize=0.1)

# plt.show()
plt.savefig('box.pdf')