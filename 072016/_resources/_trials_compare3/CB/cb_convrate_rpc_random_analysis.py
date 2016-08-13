# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 16:28:26 2016

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

test_filename  = r'cb_convrate_rpc_random_campaign_{0}.test'.format(campaignid)
vw_out_filename  = r'out_campaign_{0}.vw'.format(campaignid)
cb_analysisoutput_filename  = r'cb_analysisoutput_campaign_{0}.out'.format(campaignid)

with open(vw_out_filename, "rb") as out_vw_f:
    csvreader = csv.reader(out_vw_f, delimiter = ':')

    chosen_lps = []
    for row in csvreader:
        if len(row) == 0:
            continue
        
        chosen_lps.append(int(row[0]))

df_test = pd.read_csv(test_filename, header=None, names=['lp_map_id', 'revenue', 'conversion'])

d = {'chosen_lp' : pd.Series(chosen_lps)}
df_out = pd.DataFrame(d)

if len(df_out) != len(df_test):
    print "Length mismatch between test and out"
    sys.exit()
    
frames = [df_test, df_out]
df_result = pd.concat(frames, axis=1)

df_lp_matches = df_result[df_result.lp_map_id == df_result.chosen_lp]

clicks = len(df_lp_matches)
conversions = df_lp_matches.conversion.sum()
conversionrate= (conversions * 1.0) / clicks 

with open(cb_analysisoutput_filename, "wb") as f:
    f.write("cb_conversions, cb_clicks, cb_conversionrate\n")
    stroutput = "{0},{1},{2}\n".format(conversions, clicks, conversionrate)    
    f.write(stroutput)
