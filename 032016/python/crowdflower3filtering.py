# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 14:38:16 2016

@author: agoswami
"""

import pandas as pd
import numpy as np

## ----------- Trial 1 --------
#df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
#df['four'] = 'bar'
#df['five'] = df['one'] > 0
#df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

## ----------- Trial 2 --------
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
df['four'] = 'bar'
df['five'] = df['one'] > 0
df2 = df.copy()
df2['timestamp'] = pd.Timestamp('20120101')
df2.ix[['a','c','h'],['one','timestamp']] = np.nan
df2.ix[['a','c'],['four']] = np.nan

print 'keep rows where df2[\'four\'] is not null'
print df2[df2['four'].notnull()]

print 'drop rows with missing values'
print df2.dropna()

print 'drop columns with missing values'
print df2.dropna(axis=1)

print df2.get_dtype_counts()

#--------Trial 3 ------------
#s = pd.Series([1, 2, 3])
#s.loc[0] = None
#s.loc[1] = np.nan

# ------ Trial 4 --------------
df_score3 = pd.read_csv(r'E:\hackerreborn\032016\_resources\crowdflower3\train_map_scored3.csv')
df_score3_filtered = df_score3.dropna(
            subset=['catTop1', 'catTop2', 'catTop3', 'catTop4', 'catTop5', 'catAll', 'caption'], 
            how='all')
            
df_score3_filtered.to_csv(r'E:\hackerreborn\032016\_resources\crowdflower3\train_map_scored3_filtered2.csv', index=False)
