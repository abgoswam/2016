# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:35:38 2016

@author: agoswami
"""

import pandas as pd
import csv
from collections import defaultdict

rr_filename = r'E:\hackerreborn\2016\072016\_resources\mabtrials\data_rr.tsv'

#MAB Strategy
with open(rr_filename, 'rb') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    header = csvreader.next()
        
    dict_C = {}
    dict_CInfo = defaultdict(lambda : [0, 0]) #here we keep info about campaign: clickcount, revenuetotal
    progress = 0    
    for row in csvreader:
        progress += 1
        itembag = {}
        for i, name in enumerate(header):        
            itembag[name] = row[i]
        
        campaignid = itembag['camp_id']
        lpid = itembag['lp_id']
        revenue = float(itembag['click_leadvalue']) * float(itembag['click_lead'])
            
#        Use MAB Algo to chose the best landing page for this campaign id
        lp_MAB = None  #initialization
        if campaignid in dict_C:
            dict_LPGs = dict_C[campaignid]            

#           Using DataFrame to find best dataframe. This is because we want to sort across multiple dimensions
            df_LP = pd.DataFrame(dict_LPGs)
            df_LP = df_LP.T
            df_LP.rename(columns={0: 'clicks', 1:'leadcount', 2:'revenuetotal', 3:'rpc'}, inplace=True)
            df_LP_Sorted = df_LP.sort(['rpc', 'revenuetotal', 'leadcount', 'clicks'], ascending=False)                     
            lp_MAB = df_LP_Sorted.index[0]
        
        if lp_MAB == lpid:
            dict_CInfo[campaignid][0] += 1
            dict_CInfo[campaignid][1] += revenue
          
#        ---- Debug ---------  
#        print "{0},{1},{2}".format(campaignid, lpid, lp_MAB)     
        if progress % 1000 == 0:
             print progress
        
#        -------Update MAB table Step ---------
#        We keep the conversion count, revenue and revenue per click for that campaign, landing page combination
#        There are 4 tuples we wan to maintain for each landing page: clicks, leads, revenuetotal, revenueperclick
        if campaignid not in dict_C:
            dict_C[campaignid] = defaultdict(lambda : [0, 0, 0, 0])

        dict_C[campaignid][lpid][0] += 1
        if itembag['click_lead'] == '1':
            dict_C[campaignid][lpid][1] += 1
        dict_C[campaignid][lpid][2] += revenue
        dict_C[campaignid][lpid][3] = dict_C[campaignid][lpid][2] / dict_C[campaignid][lpid][0]
        
#        print dict_C

df_cinfo = pd.DataFrame(dict_CInfo)
df_cinfo = df_cinfo.T.reset_index()
df_cinfo.rename(columns={'index': 'camp_id', 0: 'clickcount', 1:'revenue'}, inplace=True)
df_cinfo['rpc'] = df_cinfo.revenue / df_cinfo.clickcount
df_cinfo.to_csv('algo_mab.csv', index=False)
        
#df_lpids = pd.DataFrame()
#for k in dict_C:
#    df_k = pd.DataFrame(dict_C[k])
#    df_lpids = pd.concat([df_k, df_lpids], axis=1)   

#dict1 = {1: [2,2]}  
#df_dict1 = pd.DataFrame(dict1)
#df_lpids = pd.concat([df_lpids, df_dict1], axis=1)   
        
        
        
        
        
        
        