# -*- coding: utf-8 -*-
"""
Created on Sat Jul 09 19:46:50 2016

@author: agoswami
"""

import pandas as pd
import csv
import re
from collections import defaultdict
import sys
import random

if len(sys.argv) != 2:
    print "Error in passing arguments"
    sys.exit()
    
campaignid = sys.argv[1]  
rr_filename             = r'E:\hackerreborn\2016\072016\_resources\_base\data_rr.tsv'
vw_campaign_filename    = r'campaign_{0}.vw'.format(campaignid)
test_campaign_filename  = r'campaign_{0}.test'.format(campaignid)  
tlc_train_filename      = r'campaign_{0}_tlc_train.csv'.format(campaignid)
tlc_test_filename       = r'campaign_{0}_tlc_test.csv'.format(campaignid)

df = pd.read_csv(rr_filename, delimiter='\t')
df_campaignid = df[df.camp_id == int(campaignid)]

lp_ids = df_campaignid.lp_id.unique()
lp_map = {}
for i, item in enumerate(lp_ids):
    lp_map[item] = i
    
with open(rr_filename, 'rb') as f, \
    open(vw_campaign_filename, "wb") as vw_outfile,\
    open(test_campaign_filename, "wb") as test_outfile,\
    open(tlc_train_filename, "wb") as tlc_trainfile,\
    open(tlc_test_filename, "wb") as tlc_testfile:    

    csvreader = csv.reader(f, delimiter = '\t')
    header = csvreader.next()

    lp_info = defaultdict(dict)
    
    progress = 0
    tlc_namecol = 0
    for row in csvreader:
        progress += 1
        if progress % 1000 == 0:
            print progress
            
        itembag = {}
        for idx, name in enumerate(header):
            itembag[name] = row[idx]
        
        camp_id = itembag['camp_id']
        if camp_id != campaignid:
            continue
        
        lp_id = int(itembag['lp_id'])
        lp_map_id = lp_map[lp_id]
        revenue = float(itembag['click_leadvalue']) * float(itembag['click_lead'])
        conversion_0_1 =  int(itembag['click_lead'])
        
#        output to test file
        test_line = str(lp_map_id) + "," + str(revenue) + "," + str(conversion_0_1) 
        test_outfile.write(test_line + "\n") 
       
#       We will use 2 features for each landing page : conversion rate and a random feature
        for i, item in enumerate(lp_ids):
            item_map_id = lp_map[item]
            hist_revsum      = lp_info[item_map_id].get('revsum', 0)
            hist_clickcount  = lp_info[item_map_id].get('clickcount', 0)
            hist_leadcount   = lp_info[item_map_id].get('leadcount', 0)
            hist_random      = random.uniform(0,0.004)
            
            hist_convrate = (hist_leadcount * 1.0) / (hist_clickcount + 10)
            hist_rpc = (hist_revsum * 1.0) / (hist_clickcount + 10)
            
#            VW Test
            vw_line = "| "
            vw_line += "convrate:" + str(hist_convrate) + " "
            vw_line += "rpc:" + str(hist_rpc) + " "
            vw_line += "random:" + str(hist_random) + " "
            vw_outfile.write(vw_line + "\n")

#           TLC test            
            tlc_test_line = str(tlc_namecol) + "," + str(hist_convrate) + "," + str(hist_rpc) + "," + str(hist_random) 
            tlc_testfile.write(tlc_test_line + "\n")
            tlc_namecol += 1
 
               
        if(conversion_0_1 == 1):
            label = '+1'
        else:
            label = '-1'

#       VW Model update            
        lp_info[lp_map_id]['revsum']      = lp_info[lp_map_id].get('revsum', 0) + revenue
        lp_info[lp_map_id]['clickcount']  = lp_info[lp_map_id].get('clickcount', 0) + 1
        lp_info[lp_map_id]['leadcount']   = lp_info[lp_map_id].get('leadcount', 0) + conversion_0_1
        lp_info[lp_map_id]['random']      = random.uniform(0,0.004)
        
        update_convrate = (lp_info[lp_map_id]['leadcount'] * 1.0) / (lp_info[lp_map_id]['clickcount'] + 10)
        update_rpc = (lp_info[lp_map_id]['revsum'] * 1.0) / (lp_info[lp_map_id]['clickcount'] + 10)
        
        vw_line = label + ' | '
        vw_line += 'convrate:' + str(update_convrate) + " "
        vw_line += 'rpc:' + str(update_rpc) + " "
        vw_line += "random:" + str(lp_info[lp_map_id]['random'])
        vw_outfile.write(vw_line + "\n")
        
#        TLC Train
        tlc_train_line = str(conversion_0_1) + "," + str(update_convrate) + "," + str(update_rpc) + "," + str(lp_info[lp_map_id]['random']) 
        tlc_trainfile.write(tlc_train_line + "\n")
        
        