# -*- coding: utf-8 -*-
"""
Created on Sun Jul 03 11:19:06 2016

@author: agoswami
"""

import pandas as pd
import csv
import re
from collections import defaultdict
import sys

def clean(s):
  return " ".join(re.findall(r'\w+', s,flags = re.UNICODE | re.LOCALE)).lower()
 
if len(sys.argv) != 2:
    print "Error in passing arguments"
    sys.exit()
    
campaignid = sys.argv[1]  
rr_filename = r'E:\hackerreborn\2016\072016\_resources\mabtrials\data_rr.tsv'
vw_campaign_filename = r'E:\hackerreborn\2016\072016\_resources\mabtrials\campaign_{0}.vw'.format(campaignid)
test_campaign_filename = r'E:\hackerreborn\2016\072016\_resources\mabtrials\campaign_{0}.test'.format(campaignid)  

#MAB Strategy
with open(rr_filename, 'rb') as f, \
    open(vw_campaign_filename, "wb") as vw_outfile,\
    open(test_campaign_filename, "wb") as test_outfile:
    
    csvreader = csv.reader(f, delimiter = '\t')
    header = csvreader.next()
#    print header 
    
    unique_lpids = set()
    list_lpids = [] # k
    action_revenue_click = defaultdict(lambda : [0, 0])
    k = 0
    for row in csvreader:
        k += 1
        if k % 1000 == 0:
            print k
        
        itembag = {}
        for i, value in enumerate(header):
            itembag[value] = row[i]
            
#        print row
#        print itembag
        camp_id = itembag['camp_id']
        if (camp_id != campaignid):
            continue
        
        lpid = itembag['lp_id']
        revenue = float(itembag['click_lead']) * float(itembag['click_leadvalue'])     
        if lpid not in unique_lpids:        
            unique_lpids.add(lpid) 
            list_lpids.append(lpid)
        
#        -- required for CB mode -------
        action = 1 + list_lpids.index(lpid)
        action_revenue_click[action][0] += revenue
        action_revenue_click[action][1] += 1
        
        if revenue > 0:
#            we can modify this function. For now its revenue / click
            cost = -1.0 * revenue
        else:
            cost = 0
            
        probability = 1.0 / len(unique_lpids)
        vw_line = str(action) + ":" + str(cost) + ":" +   str(probability) + " | "   

#        ---- Features --------   
        vw_line += "time:" + itembag['time'] + " "
        vw_line += "click_referer_" + clean(itembag['click_referer']).replace(" ", "_") + " "
        vw_line += "click_useragent_" + clean(itembag['click_useragent']).replace(" ", "_") + " "
        vw_line += "source_id_" + clean(itembag['source_id']).replace(" ", "_") + " "
        vw_line += "click_cpc:" + itembag['click_cpc'] + " "
        vw_line += "click_os_" + clean(itembag['click_os']).replace(" ", "_") + " "
        vw_line += "click_brand_" + clean(itembag['click_brand']).replace(" ", "_") + " "
        vw_line += "name_" + clean(itembag['name']).replace(" ", "_") + " "
        vw_line += "click_model_" + clean(itembag['click_model']).replace(" ", "_") + " "
        vw_line += "namemodel_" + clean(itembag['namemodel']).replace(" ", "_") + " "
        vw_line += "namemarketing_" + clean(itembag['namemarketing']).replace(" ", "_") + " "
        vw_line += "devicetype_" + clean(itembag['devicetype']).replace(" ", "_") + " "
        vw_line += "displaysize_" + clean(itembag['displaysize']).replace(" ", "_") + " "
        vw_line += "resolution_" + clean(itembag['resolution']).replace(" ", "_") + " "
        vw_line += "dataspeed_" + clean(itembag['dataspeed']).replace(" ", "_") + " "
        vw_line += "carrier_" + clean(itembag['carrier']).replace(" ", "_") + " "
        vw_line += "click_isp_" + clean(itembag['click_isp']).replace(" ", "_") + " "
        vw_line += "countrycode_" + clean(itembag['countrycode']).replace(" ", "_") + " "
        vw_line += "onwifi_" + clean(itembag['onwifi']).replace(" ", "_") + " "
        vw_line += "region_" + clean(itembag['region']).replace(" ", "_") + " "
        vw_outfile.write(vw_line[:-1] + "\n")
         
#        output to test file
        test_line = str(action) + "," + str(revenue) 
        test_outfile.write(test_line + "\n")
        
#        if k > 30:
#            break