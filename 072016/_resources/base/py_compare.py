# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 22:34:01 2016

@author: agoswami
"""

import pandas as pd

#Round Robin Data
df_algo_rr = pd.read_csv(r'E:\hackerreborn\2016\072016\_resources\mabtrials\algo_roundrobin.csv', header=0, names = ['camp_id', 'rr_revenue', 'rr_clickcount', 'rr_rpc'])
df_algo_rr = df_algo_rr[df_algo_rr.rr_rpc > 0]
                
#Multi Armed Bandit                
df_algo_mab = pd.read_csv(r'E:\hackerreborn\2016\072016\_resources\mabtrials\algo_mab.csv', header=0, names = ['camp_id', 'mab_clickcount', 'mab_revenue', 'mab_rpc'])
df_algo_mab = df_algo_mab[df_algo_mab.mab_rpc > 0]
                  
#Contextual bandit
df_algo_cb_1 = pd.read_csv(r'E:\hackerreborn\2016\072016\_resources\cbtrials\algo_cb_campaign_1.csv', header=0, names = ['camp_id', 'cb_clickcount', 'cb_revenue', 'cb_rpc'])
df_algo_cb_2 = pd.read_csv(r'E:\hackerreborn\2016\072016\_resources\cbtrials\algo_cb_campaign_2.csv', header=0, names = ['camp_id', 'cb_clickcount', 'cb_revenue', 'cb_rpc'])
df_algo_cb_14 = pd.read_csv(r'E:\hackerreborn\2016\072016\_resources\cbtrials\algo_cb_campaign_14.csv', header=0, names = ['camp_id', 'cb_clickcount', 'cb_revenue', 'cb_rpc'])
df_algo_cb_15 = pd.read_csv(r'E:\hackerreborn\2016\072016\_resources\cbtrials\algo_cb_campaign_15.csv', header=0, names = ['camp_id', 'cb_clickcount', 'cb_revenue', 'cb_rpc'])
df_algo_cb_64 = pd.read_csv(r'E:\hackerreborn\2016\072016\_resources\cbtrials\algo_cb_campaign_64.csv', header=0, names = ['camp_id', 'cb_clickcount', 'cb_revenue', 'cb_rpc'])

frames = [df_algo_cb_1, df_algo_cb_2, df_algo_cb_14, df_algo_cb_15, df_algo_cb_64]
df_algo_cb = pd.concat(frames)

df_inter = pd.merge(df_algo_rr, df_algo_mab, how='left', left_on='camp_id', right_on='camp_id')
df_compare = pd.merge(df_inter, df_algo_cb, how='left', left_on='camp_id', right_on='camp_id')

df_result = df_compare[['camp_id', 'rr_rpc', 'mab_rpc', 'cb_rpc']]
df_result.rename(columns={'rr_rpc': 'RPC Round Robin', 
                          'mab_rpc': 'RPC Multi Armed Bandit',
                          'cb_rpc': 'RPC Contextual Bandit'}, inplace=True)
                          
df_result.to_csv('comparison_chart.csv', index=False)