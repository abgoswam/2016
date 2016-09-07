# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 15:32:16 2016

@author: agoswami
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'_results_20090503.csv')

fig, ax = plt.subplots()

ips = df.IPS
ips_lowerbar = df.IPS - df.lowerrorinterval
ips_upperbar = df.uppererrorinterval - df.IPS

N = len(ips)
ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

rects1 = ax.bar(ind, ips, width, color='y', yerr=[ips_lowerbar, ips_upperbar])

ax.set_ylim([0.025,0.055])
ax.set_ylabel('IPS Estimates')
ax.set_title('IPS Estimates for different policies. Date: 20090503')
ax.set_xticks(ind + width/2)
ax.set_xticklabels(('Random Policy', 'Multi Armed Bandit', 'MWT without CTR', 'MWT with CTR', 'MWT with CTR (-q ::)'),
                   rotation=90)

#plt.grid()
ax.axhline(y=df[df['Sweep Info'] == 'Multi Armed Bandit'].lowerrorinterval.iloc[0], 
           linewidth=1, 
           linestyle='--',
           color='r')
ax.axhline(y=df[df['Sweep Info'] == 'Multi Armed Bandit'].uppererrorinterval.iloc[0],
           linewidth=1, 
           linestyle='--',
           color='r')
#ax.set_aspect('equal', adjustable='box') 
#plt.show()
plt.savefig('20090503.jpeg', bbox_inches='tight')