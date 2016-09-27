# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:28:23 2016

@author: agoswami
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

l = [10,11,12,10,9]

#numpy
l_arr = np.array(l)

#pandas
l_df = pd.DataFrame({'vals' : l})

mu, sigma = 10, 0.2 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

abs(mu - np.mean(s)) < 0.01
abs(sigma - np.std(s, ddof=1)) < 0.01

plt.plot(s)
plt.show()

count, bins, ignored = plt.hist(s, 30, normed=True)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()

