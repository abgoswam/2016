# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 09:27:37 2016

@author: agoswami
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'E:\hackerreborn\2016\082016\_resources\OneMLRecSysHackathon\data\hackathon-click-search-train-data-test-users.csv')
df['RequestTimeDate'] = df['RequestTime'].map(lambda x : x[0:10])

##EDA. all data
#dateCounts = df.RequestTimeDate.value_counts()
#dateCounts_sorted = dateCounts.sort_index()
#dateCounts_sorted.plot()
#
#df_counts = pd.DataFrame({'counts' : dateCounts_sorted})
#df_counts['cum_sum'] = df_counts.counts.cumsum()
#df_counts['cum_perc'] = 100* df_counts.cum_sum /df_counts.counts.sum()
#
##click data
#df_clicks = df[df.Click == '1']
#clicks_dateCounts = df_clicks.RequestTimeDate.value_counts()
#clicks_dateCounts_sorted = clicks_dateCounts.sort_index()
#clicks_dateCounts_sorted.plot()

#search data
df_search = df[df.EventType == 'Search']
df_search['Score'] = 3

#carousel data
df_carousel = df[df.EventType == 'Carousel']
df_carousel['ClickInt'] = df_carousel['Click'].astype(int)
df_carousel['PositionInt'] = df_carousel['Position'].astype(int)
df_carousel['PositionInt20'] = df_carousel['PositionInt'].map(lambda x : x if x <= 20 else 20)
## EDA
#df_positionint20 = pd.DataFrame({'counts' :df_carousel.PositionInt20.value_counts().sort_index()})
#df_positionint20['cum_sum'] = df_positionint20.counts.cumsum()
#df_positionint20['cum_perc'] = 100*df_positionint20.cum_sum /df_positionint20.counts.sum()
df_carousel['Score'] = 5 * df_carousel['ClickInt'] * df_carousel['PositionInt20']

#merge search and carousel data
frames = [df_search, df_carousel]
df_scored = pd.concat(frames)

#EDA on scores
df_scoredcounts = pd.DataFrame({'counts' :df_scored.Score.value_counts().sort_index()})
df_scoredcounts['cum_sum'] = df_scoredcounts.counts.cumsum()
df_scoredcounts['cum_perc'] = 100* df_scoredcounts.cum_sum /df_scoredcounts.counts.sum()

## EDA
#carouseldata_group_position = df_carousel.groupby(['PositionInt'])
#grouped_click = carouseldata_group_position['ClickInt']
#df_clickinfo = grouped_click.agg([np.sum, np.size])
#df_clickinfo['CTR'] = df_clickinfo['sum'] /  df_clickinfo['size']


##pandas visualization trials
#mu, sigma = 100, 15
#x = mu + sigma*np.random.randn(10000)
#
#df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),
#                    'c': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
#                    
## the histogram of the data
#n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
#
#ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#
#df1 = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
#                   'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
#                   'C' : np.random.randn(8),
#                   'D' : np.random.randn(8)})
#
#grouped = df1.groupby('A')
#grouped['C'].agg([np.sum, np.mean, np.std])
#
#df2 = pd.DataFrame({'X' : ['B', 'B', 'A', 'A'], 'Y' : [1, 2, 3, 4]})
#df2.groupby(['X'], sort=False).sum()
