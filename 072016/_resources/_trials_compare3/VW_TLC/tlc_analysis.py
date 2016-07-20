# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:09:46 2016

@author: agoswami
"""

import pandas as pd
import csv
import re
from collections import defaultdict
import sys

if len(sys.argv) != 2:
    print "Error in passing arguments"
    sys.exit()
    
campaignid = sys.argv[1] 
rr_filename                 = r'E:\hackerreborn\2016\072016\_resources\_base\data_rr.tsv'
test_campaign_filename      = r'campaign_{0}.test'.format(campaignid)
tlc_campaign_out_filename   = r'campaign_{0}_out.tlc'.format(campaignid)
ml_tlc_output_filename      = r'tlc_analysisoutput_campaign_{0}.csv'.format(campaignid)

df = pd.read_csv(rr_filename, delimiter='\t')
df_campaignid = df[df.camp_id == int(campaignid)]
df_test = pd.read_csv(test_campaign_filename, header=None, names=['lp_map_id', 'revenue', 'conversion'])

lp_ids = df_campaignid.lp_id.unique()
n = len(lp_ids)

k = 0
clickcount = 0
revenue = 0
conversioncount = 0

with open(tlc_campaign_out_filename, 'rb') as f:
    csvreader = csv.reader(f, delimiter='\t')
    header = csvreader.next()

    progress = 0
    scorevec = []    
    for row in csvreader:
        itembag = {}
        for i, name in enumerate(header):
            itembag[name] = row[i]
            
        progress += 1
        if progress % 1000 == 0:
            print progress
        
        if len(scorevec) == n:
#            print scorevec
            model_lp = scorevec.index(max(scorevec))
            test_lp = int(df_test.iloc[k]['lp_map_id'])
            
            if test_lp == model_lp:
                clickcount += 1
#                revenue += df_test.iloc[k]['revenue']
                conversioncount += df_test.iloc[k]['conversion']
            
            k += 1
            scorevec = []
            
        scorevec.append(itembag['Probability'])
        
with open(ml_tlc_output_filename, 'wb') as f:
    f.write("camp_id,tlc_clickcount,tlc_conversioncount,tlc_convrate\n")
    convrate = (conversioncount * 1.0) / clickcount
    output = "{0},{1},{2},{3}".format(campaignid, clickcount, conversioncount, convrate)
    f.write(output + '\n')   