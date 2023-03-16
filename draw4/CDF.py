from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

sns.set(palette="muted", color_codes=True)


# # arr = np.random.normal(size=100)
data = pd.read_csv('hash16_bit_Distri_FarmHash.csv')
x = data[['bitC15']]
# # plot histogram
# plt.subplot(221)
# plt.hist(arr)
#
# # obtain histogram data
# plt.subplot(222)
# hist, bin_edges = np.histogram(arr)
# plt.plot(hist)
#
# # fit histogram curve
# plt.subplot(223)
# sns.distplot(arr, kde=False, fit=stats.gamma, rug=True)

import numpy as np
import seaborn as sns

# x = np.random.randn(200)
kwargs = {'cumulative': True}
sns.distplot(x, hist_kws=kwargs, kde_kws=kwargs,color='#3CB371', bins=49, hist=True)

plt.ylabel('Density')
plt.xlabel("Different Keys")
# plt.show()
plt.savefig('CDF.pdf')