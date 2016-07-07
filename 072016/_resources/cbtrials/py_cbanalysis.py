# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 08:49:40 2016

@author: agoswami
"""

import csv
import sys
import pandas as pd

if len(sys.argv) != 2:
    print "Error in passing arguments"
    sys.exit()
    
campaignid = sys.argv[1]
vw_campaign_out_filename = r'E:\hackerreborn\2016\072016\_resources\mabtrials\campaign_{0}_out.vw'.format(campaignid)
test_campaign_filename = r'E:\hackerreborn\2016\072016\_resources\mabtrials\campaign_{0}.test'.format(campaignid)
cb_output_filename = r'E:\hackerreborn\2016\072016\_resources\mabtrials\algo_cb_campaign_{0}.csv'.format(campaignid)

df_vw_out = pd.read_csv(vw_campaign_out_filename, names = ['action'])
df_test = pd.read_csv(test_campaign_filename, names=['action', 'revenue'])

clickcount = 0
revenue = 0
for i in range(len(df_test)):
    if i % 1000 == 0:
        print i
        
    action_rr = df_test.iloc[i]['action']
    action_predicted = df_vw_out.iloc[i]['action']
    
    if action_rr == action_predicted:
        clickcount += 1
        revenue += df_test.iloc[i]['revenue']

with open(cb_output_filename, 'wb') as f:
    f.write("camp_id,clickcount,revenue,rpc\n")
    rpc = (revenue * 1.0) / clickcount
    output = "{0},{1},{2},{3}".format(campaignid, clickcount, revenue, rpc)
    f.write(output + '\n')

#with \
#    open(vw_campaign_out_filename, 'rb') as f_vw, \
#    open(test_campaign_filename, 'rb') as f_test:
#        vw_reader = csv.reader(f_vw)
#        test_reader = csv.reader(f_test, delimiter = '\t')
#
#        print "-------------"        
#        for row in vw_reader:
#            print row
#            
#        print "-------------"        
#        for row in test_reader:
#            print row
          