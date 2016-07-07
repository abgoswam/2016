# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 15:58:54 2016

@author: agoswami
"""

import pandas as pd
import numpy as np
import csv
from collections import defaultdict

rr_filename = r'E:\hackerreborn\2016\072016\_resources\mabtrials\data_rr.tsv'
df = pd.read_csv(rr_filename, sep='\t')

df['revenue'] = df.click_lead * df.click_leadvalue
grouped_campaign = df.groupby('camp_id')['revenue']

#Round Robin Strategy
df_bycampaign = grouped_campaign.agg([np.sum, np.size]).reset_index()
df_bycampaign.rename(columns={'sum': 'revenue', 'size':'clickcount'}, inplace=True)
df_bycampaign['rpc'] = df_bycampaign.revenue / df_bycampaign.clickcount

df_bycampaign.to_csv('algo_roundrobin.csv', index=False)
