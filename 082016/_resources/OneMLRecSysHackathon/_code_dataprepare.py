# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 20:52:22 2016

@author: agoswami
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'E:\hackerreborn\2016\082016\_resources\OneMLRecSysHackathon\data\hackathon-click-search-train-data-test-users.csv')
df['RequestTimeDate'] = df['RequestTime'].map(lambda x : x[0:10])

#search data
df_search = df[df.EventType == 'Search']
df_search['Score'] = 3

#carousel data
df_carousel = df[df.EventType == 'Carousel']
df_carousel['ClickInt'] = df_carousel['Click'].astype(int)
df_carousel['PositionInt'] = df_carousel['Position'].astype(int)
df_carousel['PositionInt20'] = df_carousel['PositionInt'].map(lambda x : x if x <= 20 else 20)
df_carousel['Score'] = 5 * df_carousel['ClickInt'] * df_carousel['PositionInt20']

#merge search and carousel data
frames = [df_search, df_carousel]
df_scored = pd.concat(frames)
df_scored['RandomInt'] = np.random.randint(20, size=len(df_scored))

df_train = df_scored[df_scored.RequestTimeDate < '2016-03-01']
df_test = df_scored[df_scored.RequestTimeDate >= '2016-03-01']

##mytraintest
#df_train[['UserId', 'Sid', 'Score']].to_csv(r'mytraintest\train.tsv', sep='\t', index=False)
#df_test[['UserId', 'Sid', 'Score']].to_csv(r'mytraintest\test.tsv', sep='\t', index=False)

df_train[['UserId', 'Sid', 'RandomInt']].to_csv(r'mytraintest\train.tsv', sep='\t', index=False)