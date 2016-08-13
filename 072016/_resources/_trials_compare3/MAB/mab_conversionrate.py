# -*- coding: utf-8 -*-
"""
Created on Sat Jul 09 19:06:13 2016

@author: agoswami
"""

import pandas as pd
import csv
from collections import defaultdict

rr_filename = r'E:\hackerreborn\2016\072016\_resources\_base\data_rr.tsv'
mab_filename = 'mab_analysisoutput_campaignall.out'

#MAB Strategy
with open(rr_filename, 'rb') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    header = csvreader.next()
        
    dict_C = {}
    dict_CInfo = defaultdict(lambda : [0, 0, 0]) #here we keep info about campaign: clickcount, revenuetotal, conversioncount
    progress = 0    
    for row in csvreader:
        progress += 1
        itembag = {}
        for i, name in enumerate(header):        
            itembag[name] = row[i]
        
        campaignid = itembag['camp_id']
        lpid = itembag['lp_id']
        revenue = float(itembag['click_leadvalue']) * float(itembag['click_lead'])
        conversion = int(itembag['click_lead'])
            
#        Use MAB Algo to chose the best landing page for this campaign id
        lp_MAB = None  #initialization
        if campaignid in dict_C:
            dict_LPGs = dict_C[campaignid]            

#           Using DataFrame to find best dataframe. This is because we want to sort across multiple dimensions
            df_LP = pd.DataFrame(dict_LPGs)
            df_LP = df_LP.T
            df_LP.rename(columns={0: 'clicks', 1:'leadcount', 2:'revenuetotal', 3:'rpc', 4:'convrate'}, inplace=True)
            df_LP_Sorted = df_LP.sort(['convrate'], ascending=False)                     
            lp_MAB = df_LP_Sorted.index[0]
        
        if lp_MAB == lpid:
            dict_CInfo[campaignid][0] += 1
            dict_CInfo[campaignid][1] += revenue
            dict_CInfo[campaignid][2] += conversion
            
            
        #        ---- Debug ---------  
#        print "{0},{1},{2}".format(campaignid, lpid, lp_MAB)     
        if progress % 1000 == 0:
             print progress
        
#        -------Update MAB table Step ---------
#        We keep the conversion count, revenue and revenue per click for that campaign, landing page combination
#        There are 5 tuples we wan to maintain for each landing page: 
#        clicks, leads, revenuetotal, revenueperclick, conversionrate
        if campaignid not in dict_C:
            dict_C[campaignid] = defaultdict(lambda : [0, 0, 0, 0, 0])

        dict_C[campaignid][lpid][0] += 1
        if itembag['click_lead'] == '1':
            dict_C[campaignid][lpid][1] += 1
        dict_C[campaignid][lpid][2] += revenue
        dict_C[campaignid][lpid][3] = (dict_C[campaignid][lpid][2] * 1.0) / (dict_C[campaignid][lpid][0] + 10)
        dict_C[campaignid][lpid][4] = (dict_C[campaignid][lpid][1] * 1.0) / (dict_C[campaignid][lpid][0] + 10)
        
#        break


df_cinfo = pd.DataFrame(dict_CInfo)
df_cinfo = df_cinfo.T.reset_index()
df_cinfo.rename(columns={'index': 'camp_id', 0: 'mab_clicks', 1:'mab_revenuesum', 2:'mab_conversions'}, inplace=True)
df_cinfo['rpc'] = df_cinfo.mab_revenuesum / df_cinfo.mab_clicks
df_cinfo['convrate'] = df_cinfo.mab_conversions / df_cinfo.mab_clicks
df_cinfo.to_csv(mab_filename, index=False)            
            
            
            
            
            
            
            
            
            
            
            
            
            