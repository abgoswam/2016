# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:26:16 2016

@author: agoswami
"""

import pandas as pd

df = pd.read_csv(r'E:\hackerreborn\2016\062016\_resources\TrDataExtendedSchema\JoinedInputBrandon.tsv', delimiter='\t')
df_filtered = df[(df['bucket'] == 'rr') & (df['offer_id'] != 0)][['row', 'time', 'camp_id', 'offer_id', 'lp_id', 'click_lead', 'click_leadvalue']]

df_filtered.to_csv('cb_filtered_subsetcolclone.tsv', sep='\t', index=False)