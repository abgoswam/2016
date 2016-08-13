# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:26:16 2016

@author: agoswami
"""

import pandas as pd

df = pd.read_csv(r'G:\mlworkdatasets\TrDataExtendedSchema\JoinedInputBrandon.tsv', delimiter='\t')

df_rrdata = df[df['bucket'] == 'rr']
df_rrdata.to_csv('data_rr.tsv', sep='\t', index=False)
df_rrdata.sample(frac=0.1).to_csv('data_rr_sample.tsv', sep='\t', index=False)
df_rrdata.sample(frac=0.01).to_csv('data_rr_samplesmaller.tsv', sep='\t', index=False)