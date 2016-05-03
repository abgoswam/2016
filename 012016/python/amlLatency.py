# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:52:42 2016

@author: agoswami
"""

import pandas as pd
import matplotlib.pyplot as plt

N = 100
start = 100
end = 900



df_latency1_basic_unpooled = pd.read_csv(r'latency1_basic_unpooled.csv', sep=':', header=None, names = ['static', 'latency'])                 
plt.hist(df_latency1_basic_unpooled['latency'], N, range=[start, end], normed=False, cumulative=False, label='stateless (hello world)' )     
plt.text(400, 600, r'$\mu=400$')

df_latency4_redis_unpooled_80 = pd.read_csv(r'latency4_redis_unpooled_80features.csv', sep=':', header=None, names = ['static', 'latency'])                 
plt.hist(df_latency4_redis_unpooled_80['latency'], N, range=[start, end], normed=False, cumulative=False, label='stateful (redis. 80 key lookups)' )     
plt.text(600, 400, r'$\mu=600$')

plt.title("AML Latency. Without connection pooling")
plt.xlabel( 'Latency (in ms)' )
plt.ylabel( 'Number of Calls' )
plt.grid(True)
plt.legend(loc=0)
plt.show()

df_latency1_basic_pooled = pd.read_csv(r'latency1_basic_pooled.csv', sep=':', header=None, names = ['static', 'latency'])                 
plt.hist(df_latency1_basic_pooled['latency'], N, range=[start, end], normed=False, cumulative=False, label='stateless (hello world)' )         
plt.text(220, 1300, r'$\mu=200$')

df_latency4_redis_pooled_80 = pd.read_csv(r'latency4_redis_pooled_80features.csv', sep=':', header=None, names = ['static', 'latency'])                 
plt.hist(df_latency4_redis_pooled_80['latency'], N, range=[start, end], normed=False, cumulative=False, label='stateful (redis. 80 key lookups)' )         
plt.text(430, 500, r'$\mu=400$')

plt.title("AML Latency. With connection pooling")
plt.xlabel( 'Latency (in ms)' )
plt.ylabel( 'Number of Calls' )
plt.grid(True)
plt.legend(loc=0)
plt.show()

df_latency4_redis_pooled_20 = pd.read_csv(r'latency4_redis_pooled_20features.csv', sep=':', header=None, names = ['static', 'latency'])                 
df_latency4_redis_pooled_40 = pd.read_csv(r'latency4_redis_pooled_40features.csv', sep=':', header=None, names = ['static', 'latency'])
df_latency4_redis_pooled_60 = pd.read_csv(r'latency4_redis_pooled_60features.csv', sep=':', header=None, names = ['static', 'latency'])

features20_mean_pooled = df_latency4_redis_pooled_20[df_latency4_redis_pooled_20['latency'] < 1000].mean()
features40_mean_pooled = df_latency4_redis_pooled_40[df_latency4_redis_pooled_40['latency'] < 1000].mean()
features60_mean_pooled = df_latency4_redis_pooled_60[df_latency4_redis_pooled_60['latency'] < 1000].mean()
features80_mean_pooled = df_latency4_redis_pooled_80[df_latency4_redis_pooled_80['latency'] < 1000].mean()

df_latency4_redis_unpooled_20 = pd.read_csv(r'latency4_redis_unpooled_20features.csv', sep=':', header=None, names = ['static', 'latency'])
df_latency4_redis_unpooled_40 = pd.read_csv(r'latency4_redis_unpooled_40features.csv', sep=':', header=None, names = ['static', 'latency'])
df_latency4_redis_unpooled_60 = pd.read_csv(r'latency4_redis_unpooled_60features.csv', sep=':', header=None, names = ['static', 'latency'])

features20_mean_unpooled = df_latency4_redis_unpooled_20[df_latency4_redis_unpooled_20['latency'] < 1000].mean()
features40_mean_unpooled = df_latency4_redis_unpooled_40[df_latency4_redis_unpooled_40['latency'] < 1000].mean()
features60_mean_unpooled = df_latency4_redis_unpooled_60[df_latency4_redis_unpooled_60['latency'] < 1000].mean()
features80_mean_unpooled = df_latency4_redis_unpooled_80[df_latency4_redis_unpooled_80['latency'] < 1000].mean()

stateless_pooled = [200, 200, 200, 200]
stateless_unpooled = [400, 400, 400, 400]
redismeanlatencies_pooled = [features20_mean_pooled, features40_mean_pooled, features60_mean_pooled, features80_mean_pooled]
redismeanlatencies_unpooled = [features20_mean_unpooled, features40_mean_unpooled, features60_mean_unpooled, features80_mean_unpooled]
numberfeatures = [20, 40, 60, 80]


plt.plot(numberfeatures, redismeanlatencies_pooled, 'bo-', label='stateful (with connection pooling)')
#plt.plot(numberfeatures, stateless_pooled, 'bo--', label='stateless (with connection pooling)')
plt.plot(numberfeatures, redismeanlatencies_unpooled, 'ro-', label='stateful (without connection pooling)')
#plt.plot(numberfeatures, stateless_unpooled, 'ro--', label='stateless (without connection pooling)')

plt.title("Mean client side latency v/s Number of Key lookups (Redis)")
plt.ylabel( 'Mean client latency (in ms)' )
plt.xlabel( 'Number of key lookups (Redis)' )
plt.grid(True)
plt.axis([0, 100, 0, 1000])
plt.legend(loc=0)
plt.show()