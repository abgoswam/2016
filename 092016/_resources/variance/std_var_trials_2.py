# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 09:39:32 2016

@author: agoswami
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('std_var.debug', header=None, names=['ips','reward','probability'])

df_sample = df.sample(frac=.1)
df_sample_ips_copy = df_sample['ips'].copy()

df_sample_ips_copy
plt.plot(df_sample_ips_copy)
plt.show()

#see how the plot changes when we sort
#so what we conclude is that in the above plot, the 0 values were being drowned out
df_sample_ips_copy.sort()
plt.plot(df_sample_ips_copy)
plt.show()

#interestingly for the hist, it sometimes fails with 'KeyError : 0'.
#the fix for this is to give .values
plt.hist(df_sample_ips_copy.values, 30, normed=False)
plt.show()

#Another Visualization of pandas dataframes.
df2 = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))

df2.plot()
plt.show()

plt.plot(df2['C'])
plt.show()