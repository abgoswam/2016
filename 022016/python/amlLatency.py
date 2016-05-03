# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:52:42 2016

@author: agoswami
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

N = 100
start = 100
end = 900


df_latency1_basic_pooled = pd.read_csv(r'latency1_basic_pooled.csv', sep=':', header=None, names = ['static', 'latency'])                 
plt.hist(df_latency1_basic_pooled['latency'], N, range=[start, end], normed=True, cumulative=False, label='stateless (hello world)' )         
plt.text(200, 0.03, r'$\mu=200$')

df_latency5_redispipeline_pooled_80 = pd.read_csv(r'latency5_redispipeline_pooled_80features.csv', sep=':', header=None, names = ['static', 'latency'])                 
plt.hist(df_latency5_redispipeline_pooled_80['latency'], N, range=[start, end], normed=True, cumulative=False, label='stateful. redis with pipeline (80 keys)' )         
plt.text(240, 0.025, r'$\mu=240$')

df_latency4_redis_pooled_80 = pd.read_csv(r'latency4_redis_pooled_80features.csv', sep=':', header=None, names = ['static', 'latency'])                 
plt.hist(df_latency4_redis_pooled_80['latency'], N, range=[start, end], normed=True, cumulative=False, label='stateful. redis without pipeline (80 keys)' )         
plt.text(410, 0.010, r'$\mu=410$')

plt.title("AML Latency. With connection pooling")
plt.xlabel( 'Latency (in ms)' )
plt.ylabel( 'Fraction of Calls' )
plt.axis([start, end, 0, 0.05])
plt.grid(True)
plt.legend(loc=0)
plt.show()


mean_pooled_stateless = df_latency1_basic_pooled[df_latency1_basic_pooled['latency'] < 1000]['latency'].mean()
features80_mean_pooled_redispipeline = df_latency5_redispipeline_pooled_80[df_latency5_redispipeline_pooled_80['latency'] < 1000]['latency'].mean()
features80_mean_pooled_redis = df_latency4_redis_pooled_80[df_latency4_redis_pooled_80['latency'] < 1000]['latency'].mean()

objects = ('stateless (hello world)', 'stateful. redis with pipeline (80 keys)', 'stateful. redis without pipeline (80 keys)')

y = [ mean_pooled_stateless, features80_mean_pooled_redispipeline, features80_mean_pooled_redis]
y_pos = np.arange(len(objects))
  
plt.barh(y_pos, y, align='center', alpha=0.5)  
plt.yticks(y_pos, objects)

plt.title("AML Latency. (with connection pooling)")
plt.xlabel( 'Average Latency (in ms)' )
#plt.ylabel( 'Fraction of Calls' )
#plt.axis([start, end, 0, 0.05])
plt.grid(True)
plt.legend(loc=0)
plt.show()


