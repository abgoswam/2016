# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:44:51 2016

@author: agoswami
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# MAB
df_mab = pd.read_csv(r'MAB\mab_analysisoutput_campaignall.out',
                     header=0, 
                     names = ['camp_id','mab_clicks','mab_revenue','mab_conversions','mab_rpc','mab_convrate'])
                          
df_mab = df_mab[(df_mab.camp_id == 1) | 
            (df_mab.camp_id == 2) | 
            (df_mab.camp_id == 14) | 
            (df_mab.camp_id == 15)]
            
# CB
df_cb_c1  = pd.read_csv(r'CB\cb_analysisoutput_campaign_1.out', header=0, names = ['cb_conversions', 'cb_clicks', 'cb_convrate'])
df_cb_c1['camp_id'] = 1

df_cb_c2  = pd.read_csv(r'CB\cb_analysisoutput_campaign_2.out', header=0, names = ['cb_conversions', 'cb_clicks', 'cb_convrate'])
df_cb_c2['camp_id'] = 2

df_cb_c14 = pd.read_csv(r'CB\cb_analysisoutput_campaign_14.out', header=0, names = ['cb_conversions', 'cb_clicks', 'cb_convrate'])
df_cb_c14['camp_id'] = 14

df_cb_c15 = pd.read_csv(r'CB\cb_analysisoutput_campaign_15.out', header=0, names = ['cb_conversions', 'cb_clicks', 'cb_convrate'])
df_cb_c15['camp_id'] = 15

frames = [df_cb_c1, df_cb_c2, df_cb_c14, df_cb_c15]
df_cb = pd.concat(frames)

#VW
df_vw_c1  = pd.read_csv(r'VW_TLC\vw_analysisoutput_campaign_1.csv')
df_vw_c2  = pd.read_csv(r'VW_TLC\vw_analysisoutput_campaign_2.csv')
df_vw_c14 = pd.read_csv(r'VW_TLC\vw_analysisoutput_campaign_14.csv')
df_vw_c15 = pd.read_csv(r'VW_TLC\vw_analysisoutput_campaign_15.csv')

frames = [df_vw_c1, df_vw_c2, df_vw_c14, df_vw_c15]
df_vw = pd.concat(frames)

#TLC
df_tlc_c1  = pd.read_csv(r'VW_TLC\tlc_analysisoutput_campaign_1.csv')
df_tlc_c2  = pd.read_csv(r'VW_TLC\tlc_analysisoutput_campaign_2.csv')
df_tlc_c14 = pd.read_csv(r'VW_TLC\tlc_analysisoutput_campaign_14.csv')
df_tlc_c15 = pd.read_csv(r'VW_TLC\tlc_analysisoutput_campaign_15.csv')

frames = [df_tlc_c1, df_tlc_c2, df_tlc_c14, df_tlc_c15]
df_tlc = pd.concat(frames)

#Joins
df_temp = pd.merge(df_mab, df_cb, how='left', left_on='camp_id', right_on='camp_id')
df_temp = pd.merge(df_temp, df_vw, how='left', left_on='camp_id', right_on='camp_id')
df_temp = pd.merge(df_temp, df_tlc, how='left', left_on='camp_id', right_on='camp_id')

df_all = df_temp
df_all.to_csv(r'analysis_results.csv', sep=',', index=False)

#visualizations
df_analysis = df_all[['camp_id', 'mab_convrate', 'cb_convrate', 'vw_convrate', 'tlc_convrate']]
df_analysis.rename(columns={
    'camp_id': 'CampaignId',
    'mab_convrate': 'MAB' , 
    'cb_convrate' : 'CB',
    'vw_convrate' : 'VW',
    'tlc_convrate' : 'TLC'}, inplace=True)

df_analysis = df_analysis.set_index('CampaignId')
df_analysis = df_analysis.loc[[1, 2]]

ax1 = df_analysis.plot(kind='bar', title = 'comparison of conversion rate across algos')
ax1.set_ylim(0, 0.003)
plt.ylabel('conversion rate')
plt.grid(True)

#width = 0.15
#ind = np.arange(len(df_analysis['mab_convrate']))
#plt.bar(ind, df_analysis['mab_convrate'].values, width, color='r')
#plt.bar(ind + width, df_analysis['cb_convrate'].values, width, color='y')
#plt.bar(ind + 2*width, df_analysis['vw_convrate'].values, width, color='b')
#plt.bar(ind + 3*width, df_analysis['tlc_convrate'].values, width, color='g')
#plt.show()











