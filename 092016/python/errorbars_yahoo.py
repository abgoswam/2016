# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 15:32:16 2016

@author: agoswami
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'E:\hackerreborn\2016\082016\_resources\yahoodataset\R6\20090503_full\_results_20090503.csv')

fig, ax = plt.subplots()

ips = df.IPS
ips_lowerbar = df.IPS - df.lowerrorinterval
ips_upperbar = df.uppererrorinterval - df.IPS

N = len(ips)
ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

rects1 = ax.bar(ind, ips, width, color='y', yerr=[ips_lowerbar, ips_upperbar])

ax.set_ylabel('IPS Estimates')
ax.set_title('IPS Estimates for different policies. Date: 20090503')
ax.set_xticks(ind + width/2)
ax.set_xticklabels(('without CTR', 'with CTR', 'with CTR (-q ::)'))

