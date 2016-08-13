# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 08:39:01 2016

@author: agoswami
"""

import pandas as pd
import csv
from collections import defaultdict
import random
import sys

if len(sys.argv) != 2:
    print "Error in passing arguments"
    sys.exit()

campaignid = sys.argv[1]  
rr_filename         = r'E:\hackerreborn\2016\072016\_resources\_base\data_rr.tsv'
cb_train_filename   = r'cb_convrate_rpc_random_campaign_{0}.vw'.format(campaignid)
test_filename       = r'cb_convrate_rpc_random_campaign_{0}.test'.format(campaignid) 

df = pd.read_csv(rr_filename, delimiter='\t')
df_campaignid = df[df.camp_id == int(campaignid)]

lp_ids = df_campaignid.lp_id.unique()

with open(rr_filename, 'rb') as f, \
    open(test_filename, "wb") as cb_test_outfile,\
    open(cb_train_filename, "wb") as cb_train_outfile:
        
    csvreader = csv.reader(f, delimiter = '\t')
    header = csvreader.next()
    lp_info = defaultdict(dict)
    
    progress = 0    
    for row in csvreader:
        progress += 1
        if progress % 1000 == 0:
            print progress
            
        itembag = {}
        for i, name in enumerate(header):        
            itembag[name] = row[i]
            
        camp_id = itembag['camp_id']
        if camp_id != campaignid:
            continue        
        
        lpid = int(itembag['lp_id'])
        revenue = float(itembag['click_leadvalue']) * float(itembag['click_lead'])
        conversion_0_1 = int(itembag['click_lead'])

        vw_line = ""
        for idx, item in enumerate(lp_ids):
            subline = ""

            hist_revsum      = lp_info[item].get('revsum', 0)
            hist_clickcount  = lp_info[item].get('clickcount', 0)
            hist_leadcount   = lp_info[item].get('leadcount', 0)
            
            convrate = (hist_leadcount * 1.0) / (hist_clickcount + 10)
            rpc = (hist_revsum * 1.0) / (hist_clickcount + 10)

            if item == lpid :
                # output to test file
                test_line = str(idx) + "," + str(revenue) + "," + str(conversion_0_1) 
                cb_test_outfile.write(test_line + "\n")
                
#                create VW multiline example
                probability = 1.0 / len(lp_ids)
                cost = 0
                if conversion_0_1 > 0:
                    cost = -1

                subline += "0:" + str(cost) + ":" + str(probability) + " "  
                
                lp_info[item]['revsum']      = hist_revsum + revenue
                lp_info[item]['clickcount']  = hist_clickcount + 1
                lp_info[item]['leadcount']   = hist_leadcount + conversion_0_1

            subline += "| " + "convrate:" + str(convrate) + " rpc:" + str(rpc) + " random:" + str(random.uniform(0,0.004)) + "\n"  
            vw_line += subline
        
        cb_train_outfile.write(vw_line + "\n")

#        if progress == 4:
#            break
        
        
        
        
        
        
        
        
        
        
        
        
        
    